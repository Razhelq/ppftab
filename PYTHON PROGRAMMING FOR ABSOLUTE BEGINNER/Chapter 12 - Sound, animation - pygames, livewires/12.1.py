# <Material from the book in polish
# Astrocrash08
# My modification will add new typies of the asteroids.

# Dodaj obiekt klasy Game w celu uzupełnienia programu

import math, random
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Wrapper(games.Sprite):
    """ Duszek, którego tor lotu owija się wokół ekranu. """
    def update(self):
        """ Przenieś duszka na przeciwległy brzeg ekranu. """    
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Zniszcz się. """
        self.destroy()


class Collider(Wrapper):
    """ Obiekt klasy Wrapper, który może zderzyć się z innym obiektem. """
    def update(self):
        """ Sprawdź, czy duszki nie zachodzą na siebie. """
        super(Collider, self).update()
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()               

    def die(self):
        """ Zniszcz się i pozostaw po sobie eksplozję. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Asteroid(Wrapper):
    """ Asteroida przelatująca przez ekran. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL  : games.load_image("asteroida_mala.bmp"),
              MEDIUM : games.load_image("asteroida_sred.bmp"),
              LARGE  : games.load_image("asteroida_duza.bmp") }

    SPEED = 2
    SPAWN = 2
    POINTS = 30
    
    total =  0
      
    def __init__(self, game, x, y, size):
        """ Inicjalizuj duszka asteroidy. """
        Asteroid.total += 1
        
        super(Asteroid, self).__init__(
            image = Asteroid.images[size],
            x = x, y = y,
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size, 
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.game = game
        self.size = size

    def die(self):
        """ Zniszcz asteroidę. """
        Asteroid.total -= 1

        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10   
        
        # jeśli nie jest to mała asteroida, zastąp ją dwoma mniejszymi
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_asteroid)

        # jeśli wszystkie asteroidy zostały zniszczone, przejdź do następnego poziomu    
        if Asteroid.total == 0:
            self.game.advance()

        super(Asteroid, self).die()


class Strong_asteroid(Wrapper):
    SPEED = 2
    SPAWN = 1
    POINTS = 25

    


class Ship(Collider):
    """ Statek kosmiczny gracza. """
    image = games.load_image("statek.bmp")
    sound = games.load_sound("przyspieszenie.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    VELOCITY_MAX = 3
    MISSILE_DELAY = 25

    def __init__(self, game, x, y):
        """ Inicjalizuj duszka statku. """
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.game = game
        self.missile_wait = 0

    def update(self):
        """ Obracaj statek, przyśpieszaj i wystrzeliwuj pociski, zależnie od naciśniętych klawiszy. """
        super(Ship, self).update()
        
        # obróć statek zależnie od naciśniętych klawiszy strzałek (w prawo lub w lewo)
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        # zastosuj siłę ciągu przy naciśniętym klawiszu strzałki w górę        
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            
            # zmień składowe prędkości w zależności od kąta położenia statku
            angle = self.angle * math.pi / 180  # zamień na radiany
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

            # ogranicz prędkość w każdym kierunku
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            
        # jeśli czekasz, aż statek będzie mógł wystrzelić następny pocisk,
        # zmniejsz czas oczekiwania
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        # wystrzel pocisk, jeśli klawisz spacji jest naciśnięty i skończył się
        # czas oczekiwania    
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)        
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """ Zniszcz statek i zakończ grę. """
        self.game.end()
        super(Ship, self).die()


class Missile(Collider):
    """ Pocisk wystrzelony przez statek gracza. """
    image = games.load_image("pocisk.bmp")
    sound = games.load_sound("pocisk.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Inicjalizuj duszka pocisku. """
        Missile.sound.play()
        
        # zamień na radiany
        angle = ship_angle * math.pi / 180  

        # oblicz pozycję początkową pocisku  
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # oblicz składowe prędkości pocisku
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # utwórz pocisk
        super(Missile, self).__init__(image = Missile.image,
                                      x = x, y = y,
                                      dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Obsługuj ruch pocisku. """
        super(Missile, self).update()
        
        # zniszcz pocisk, jeśli wyczerpał się jego czas życia   
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    """ Animacja eksplozji. """
    sound = games.load_sound("eksplozja.wav")
    images = ["eksplozja1.bmp",
              "eksplozja2.bmp",
              "eksplozja3.bmp",
              "eksplozja4.bmp",
              "eksplozja5.bmp",
              "eksplozja6.bmp",
              "eksplozja7.bmp",
              "eksplozja8.bmp",
              "eksplozja9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()


class Game(object):
    """ Sama gra. """
    def __init__(self):
        """ Inicjalizuj obiekt klasy Game. """
        # ustaw poziom
        self.level = 0

        # załaduj dźwięk na podniesienie poziomu
        self.sound = games.load_sound("poziom.wav")

        # utwórz wynik punktowy
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        # utwórz statek kosmiczny gracza
        self.ship = Ship(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """ Przeprowadź grę. """
        # rozpocznij odtwarzanie tematu muzycznego
        games.music.load("temat.mid")
        games.music.play(-1)

        # załaduj i ustaw tło
        nebula_image = games.load_image("mglawica.jpg")
        games.screen.background = nebula_image

        # przejdź do poziomu 1
        self.advance()

        # rozpocznij grę
        games.screen.mainloop()

    def advance(self):
        """ Przejdź do następnego poziomu gry. """
        self.level += 1
        
        # wielkość obszaru ochronnego wokół statku przy tworzeniu asteroid
        BUFFER = 150
     
        # utwórz nowe asteroidy 
        for i in range(self.level):
            # oblicz współrzędne x i y zapewniające minimum odległości od statku
            # określ minimalną odległość wzdłuż osi x oraz wzdłuż osi y
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # wyznacz odległość wzdłuż osi x oraz wzdłuż osi y
            # z zachowaniem odległości minimalnej
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # oblicz położenie na podstawie odległości
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            # jeśli to konieczne, przeskocz między krawędziami ekranu
            x %= games.screen.width
            y %= games.screen.height
       
            # utwórz asteroidę
            new_asteroid = Asteroid(game = self,
                                    x = x, y = y,
                                    size = Asteroid.LARGE)

            # my new asteroid
            strong_asteroid = Strong_asteroid(game = self,
                                              x = x,
                                              y = y)
                                                        
            games.screen.add(new_asteroid)

        # wyświetl numer poziomu
        level_message = games.Message(value = "Poziom " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        # odtwórz dźwięk przejścia do nowego poziomu (nie dotyczy pierwszego poziomu)
        if self.level > 1:
            self.sound.play()
            
    def end(self):
        """ Zakończ grę. """
        # pokazuj komunikat 'Koniec gry' przez 5 sekund
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()

# wystartuj!
main()
