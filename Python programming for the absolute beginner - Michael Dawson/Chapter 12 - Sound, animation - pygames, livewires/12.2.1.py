# Simos says type of game
# Player needs to repeat different combinations of colors and sounds

# Just began. Not finished
# Boolean paraworking version

import math, random
from livewires import games, color

games.init(screen_width = 1400, screen_height = 480, fps = 50)


class Button(games.Sprite):
    
    red_light = 1
    red_dark = 6
    black_light = 2
    black_dark = 7
    green_light = 3
    green_dark = 8
    blue_light = 4
    blue_dark = 9
    yellow_light = 5
    yellow_dark = 10
    new_butts = [False, False, False, False, False]
    choice = 0

    images = {red_light    : games.load_image("red_light.jpg", transparent = False),
              red_dark     : games.load_image("red_dark.jpg", transparent = False),
              black_light  : games.load_image("black_light.jpg", transparent = False),
              black_dark   : games.load_image("black_dark.jpg", transparent = False),
              green_light  : games.load_image("green_light.jpg", transparent = False),
              green_dark   : games.load_image("green_dark.png", transparent = False),
              blue_light   : games.load_image("blue_light.png", transparent = False),
              blue_dark    : games.load_image("blue_dark.png", transparent = False),
              yellow_light : games.load_image("yellow_light.png", transparent = False),
              yellow_dark  : games.load_image("yellow_dark.jpg", transparent = False)}
  
    def __init__(self, game, x, y, color):
        super(Button, self).__init__(image = Button.images[color],
                                     x = x,
                                     y = y)

        self.game = game
        self.color = color

    def update(self):
        super(Button, self).update()

        if games.keyboard.is_pressed(games.K_c):
            one = New_Button(game = self, x = 200, y = 240, color = 1)
            sound = games.load_sound("eksplozja.wav")
            sound.play()
            games.screen.add(one)
            Button.new_butts[0] = True
            Button.choice += 1
        elif games.keyboard.is_pressed(games.K_v):
            two = New_Button(game = self, x = 450, y = 240, color = 2)
            sound = games.load_sound("pocisk.wav")
            sound.play()
            games.screen.add(two)
            Button.new_butts[1] = True
            Button.choice += 1
        elif games.keyboard.is_pressed(games.K_b):
            three = New_Button(game = self, x = 700, y = 240, color = 3)
            sound = games.load_sound("przyspieszenie.wav")
            sound.play()
            games.screen.add(three)
            Button.new_butts[2] = True
            Button.choice += 1
        elif games.keyboard.is_pressed(games.K_n):
            four = New_Button(game = self, x = 950, y = 240, color = 4)
            sound = games.load_sound("poziom.wav")
            sound.play()
            games.screen.add(four)
            Button.new_butts[3] = True
            Button.choice += 1
        elif games.keyboard.is_pressed(games.K_m):
            five = New_Button(game = self, x = 1200, y = 240, color = 5)
            games.screen.add(five)
            Button.new_butts[4] = True
            Button.choice += 1
    

class Master(games.Sprite):
    new_butts = [False, False, False, False, False]

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
                Master.new_butts[0] = True
            elif self.number == 1:
                two = New_Button(game = self, x = 450, y = 240, color = 2)
                sound = games.load_sound("pocisk.wav")
                sound.play()
                games.screen.add(two)
                Master.new_butts[1] = True
            elif self.number == 2:
                three = New_Button(game = self, x = 700, y = 240, color = 3)
                sound = games.load_sound("przyspieszenie.wav")
                sound.play()
                games.screen.add(three)
                Master.new_butts[2] = True
            elif self.number == 3:
                four = New_Button(game = self, x = 950, y = 240, color = 4)
                sound = games.load_sound("poziom.wav")
                sound.play()
                games.screen.add(four)
                Master.new_butts[3] = True
            elif self.number == 4:
                five = New_Button(game = self, x = 1200, y = 240, color = 5)
                games.screen.add(five)
                Master.new_butts[4] = True
                                        
            self.delay = 50
            self.level -= 1
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
                self.delay = 100
                Game.color = 1
                Master.new_butts = [False, False, False, False, False]
                Button.new_butts = [False, False, False, False, False]
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

        Master.new_butts = [False, False, False, False, False]
        
        Button.new_butts = [False, False, False, False, False]

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
                                                           
                                     

                                    

    
        
                                     
                                    
                                












































                                

        


        
                            
        
    

        
