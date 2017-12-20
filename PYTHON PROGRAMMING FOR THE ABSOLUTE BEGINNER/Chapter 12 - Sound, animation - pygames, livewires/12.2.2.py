# Simos says type of game
# Player needs to repeat different combinations of colors and sounds

# Just began. Not finished
# Trying to fix the boolean method from 12.2.1, still in progress.

import math, random
from livewires import games, color

games.init(screen_width = 1400, screen_height = 480, fps = 50)


class Button(games.Sprite):
    
    red_light = 1
    black_light = 2
    green_light = 3
    blue_light = 4
    yellow_light = 5
    new_butts = []
    choice = 0

    images = {red_light    : games.load_image("red_light.jpg", transparent = False),
              black_light  : games.load_image("black_light.jpg", transparent = False),
              green_light  : games.load_image("green_light.jpg", transparent = False),
              blue_light   : games.load_image("blue_light.png", transparent = False),
              yellow_light : games.load_image("yellow_light.png", transparent = False)}

  
    def __init__(self, game, x, y, color):
        super(Button, self).__init__(image = Button.images[color],
                                     x = x,
                                     y = y)

        self.game = game
        self.color = color
        self.c = 0
        self.v = 0
        self.b = 0
        self.n = 0
        self.m = 0
        self.delay = 0
        

    def update(self):
        super(Button, self).update()

        if games.keyboard.is_pressed(games.K_c):
            one = New_Button(game = self, x = 200, y = 240, color = 1)
            sound = games.load_sound("poziom.wav")
            sound.play()
            games.screen.add(one)
            self.delay = 0
            butt = "c"
            if self.c == 0 and self.delay <= 0:
                self.delay = 1
                Button.new_butts.append(butt)
                self.c = 1
                self.v = 0
                self.b = 0
                self.n = 0
                self.m = 0
            elif self.c == 0 and self.delay > 0:
                self.delay -= 1
            Button.choice += 1
        elif games.keyboard.is_pressed(games.K_v):
            two = New_Button(game = self, x = 450, y = 240, color = 2)
            sound = games.load_sound("poziom.wav")
            sound.play()
            games.screen.add(two)
            self.delay = 0
            butt = "v"
            if self.v == 0 and self.delay <= 0:
                self.delay = 2
                Button.new_butts.append(butt)
                self.v = 1
                self.c = 0
                self.b = 0
                self.n = 0
                self.m = 0
            elif self.v == 0 and self.delay > 0:
                self.delay -= 1
            Button.choice = 1
        elif games.keyboard.is_pressed(games.K_b):
            three = New_Button(game = self, x = 700, y = 240, color = 3)
            sound = games.load_sound("poziom.wav")
            sound.play()
            games.screen.add(three)
            self.delay = 0
            butt = "b"
            if self.b == 0 and self.delay <= 0:
                self.delay = 2
                Button.new_butts.append(butt)
                self.b = 1
                self.c = 0
                self.v = 0
                self.n = 0
                self.m = 0
            elif self.b == 0 and self.delay > 0:
                self.delay -= 1
            Button.choice = 1
        elif games.keyboard.is_pressed(games.K_n):
            four = New_Button(game = self, x = 950, y = 240, color = 4)
            sound = games.load_sound("poziom.wav")
            sound.play()
            games.screen.add(four)
            self.delay = 0
            butt = "n"
            if self.n == 0 and self.delay <= 0:
                self.delay = 2
                Button.new_butts.append(butt)
                self.n = 1
                self.v = 0
                self.b = 0
                self.c = 0
                self.m = 0
            elif self.n == 0 and self.delay > 0:
                self.delay -= 1
            Button.choice = 1
        elif games.keyboard.is_pressed(games.K_m):
            five = New_Button(game = self, x = 1200, y = 240, color = 5)            
            sound = games.load_sound("poziom.wav")
            games.screen.add(five)
            self.delay = 0
            butt = "m"
            if self.m == 0 and self.delay <= 0:
                self.delay = 2
                Button.new_butts.append(butt)
                self.m = 1
                self.v = 0
                self.b = 0
                self.n = 0
                self.c = 0
            elif self.m == 0 and self.delay > 0:
                self.delay -= 1
            Button.choice = 1
        level_messageoo = games.Message(value = Button.new_butts,
                                       size = 30,
                                       color = color.yellow,
                                       x = games.screen.width/2,
                                       y = 450,
                                       lifetime = games.screen.fps,
                                       is_collideable = False)
        games.screen.add(level_messageoo)
    

class Master(games.Sprite):
    new_butts = []

    def __init__(self, game, x, y, level):
        super(Master, self).__init__(image = games.load_image("asteroid_strong.png"),
                                     x = x,
                                     y = y)
        self.delay = 50
        self.number = 0
        self.game = game
        self.level = level
        self.delay_two = 200
        
    def update(self):
        
        if self.delay > 0:
            self.delay -= 1
        elif self.delay == 0 and self.level > 0:
            self.number = random.randrange(5)
            if self.number == 0:
                one = New_Button(game = self, x = 200, y = 240, color = 1)
                sound = games.load_sound("eksplozja.wav")
                sound.play()
                games.screen.add(one)
                butt = "c"
                for i in range(5):
                    Master.new_butts.append(butt)
            elif self.number == 1:
                two = New_Button(game = self, x = 450, y = 240, color = 2)
                sound = games.load_sound("pocisk.wav")
                sound.play()
                games.screen.add(two)
                butt = "v"
                for i in range(5):
                    Master.new_butts.append(butt)
            elif self.number == 2:
                three = New_Button(game = self, x = 700, y = 240, color = 3)
                sound = games.load_sound("przyspieszenie.wav")
                sound.play()
                games.screen.add(three)
                butt = "b"
                for i in range(5):
                    Master.new_butts.append(butt)
            elif self.number == 3:
                four = New_Button(game = self, x = 950, y = 240, color = 4)
                sound = games.load_sound("poziom.wav")
                sound.play()
                games.screen.add(four)
                butt = "n"
                for i in range(5):
                    Master.new_butts.append(butt)
            elif self.number == 4:
                five = New_Button(game = self, x = 1200, y = 240, color = 5)
                games.screen.add(five)
                butt = "m"
                for i in range(5):
                    Master.new_butts.append(butt)
                                        
            self.delay = 50
            self.level -= 1
        level_messageo = games.Message(value = Master.new_butts,
                                      size = 30,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = 350,
                                      lifetime = games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_messageo)
        self.check_status()
        
    def check_status(self):

        if Master.new_butts == Button.new_butts and Button.choice > 0:
            
            level_message = games.Message(value = "Level " + str(int(Game.level) - 1),
                                              size = 60,
                                              color = color.yellow,
                                              x = games.screen.width/2,
                                              y = 50,
                                              lifetime = 5 * games.screen.fps,
                                              is_collideable = False)
            games.screen.add(level_message)
            
            if self.delay_two <= 0:
                self.game.score.value += 10
                
                Game.level += 1              
                    
                self.delay_two = 200
                self.delay = 50
                Game.color = 1
                Master.new_butts = []
                Button.new_butts = []
                Button.choice = 0
                self.game.play()
                
            elif self.delay_two > 0:
                self.delay_two -= 1

                                           
class New_Button(games.Sprite):

    red_dark = 1
    black_dark = 2
    green_dark = 3
    blue_dark = 4
    yellow_dark = 5

    images = {red_dark     : games.load_image("red_dark.jpg", transparent = False),
              black_dark   : games.load_image("black_dark.jpg", transparent = False),
              green_dark   : games.load_image("green_dark.jpg", transparent = False),
              blue_dark    : games.load_image("blue_dark.jpg", transparent = False),
              yellow_dark  : games.load_image("yellow_dark.jpg", transparent = False)}
          
    LIFETIME = 10
    
    def __init__(self, game, x, y, color):
        super(New_Button, self).__init__(image = New_Button.images[color],
                                         x = x,
                                         y = y)
        self.game = game        
        self.lifetime = New_Button.LIFETIME
        self.color = color

    def update(self):
        super(New_Button,self).update()
                 
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
        
class Game(object):
    
    color = 1
    level = 3
    
    def __init__(self):
        
        self.sound = games.load_sound("poziom.wav")

        self.score = games.Text(value = 0,
                               size = 30,
                               color = color.white,
                               top = 5,
                               right = games.screen.width - 10)

        games.screen.add(self.score)

        level_message = games.Message(value = "Level 1",
                                              size = 60,
                                              color = color.yellow,
                                              x = games.screen.width/2,
                                              y = 50,
                                              lifetime = 5 * games.screen.fps,
                                              is_collideable = False)
        games.screen.add(level_message)


    def play(self):

        wallpaper = games.load_image("db.png", transparent = False)
        games.screen.background = wallpaper

        self.advance()

        games.screen.mainloop()

    def advance(self):

        Button.choice = 0

        Master.new_butts = []
        
        Button.new_butts = []

        self.location = 100
        for i in range(5):
            new_button = Button(game = self,
                                x = self.location + 100,
                                y = 240,
                                color = Game.color)
            games.screen.add(new_button)
            self.location += 250
            Game.color += 1

        master = Master(game = self, x = 10, y = 10, level = Game.level)
        games.screen.add(master)
        
        
def main():
    simon = Game()
    simon.play()

main()
                                                           
                                     

                                    

    
        
                                     
                                    
                                












































                                

        


        
                            
        
    

        
