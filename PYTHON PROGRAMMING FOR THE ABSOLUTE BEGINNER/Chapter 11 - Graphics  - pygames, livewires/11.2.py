# The player need to aviod pizzas falling down from the skies.

from livewires import games, color
import random

games.init(screen_width = 1800, screen_height = 1000, fps = 50)


class Player(games.Sprite):
    image = games.load_image("kucharz.bmp")

    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
        
        self.time_til_drop = 0

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_collision()
        self.drop()

    def check_collision(self):
        for pizza in self.overlapping_sprites:
            pizza.collision()
            self.destroy()
            self.end_game()

    def end_game(self):
        end_message = games.Message(value = "Game over",
                                    size = 180,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen. height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

    def drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            position = random.randrange(1800)
            new_pizza = Pizza(x = position)
            games.screen.add(new_pizza)

            self.time_til_drop = int(new_pizza.height * 2.3 / Pizza.speed) + 1


class Pizza(games.Sprite):
    image = games.load_image("pizza.bmp")
    speed = 1

    def __init__(self, x = 0, y = 0):
        super(Pizza, self).__init__(image = Pizza.image,
                                   x = x,
                                   y = y,
                                   dy = Pizza.speed)

        Pizza.speed += 0.02        
     
    def collision(self):
        self.destroy()
            
def main():
    wall_image = games.load_image("sky.jpg", transparent = False)
    games.screen.background = wall_image

    player = Player()
    games.screen.add(player)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

main()
        
            
        
        


                                   
    
