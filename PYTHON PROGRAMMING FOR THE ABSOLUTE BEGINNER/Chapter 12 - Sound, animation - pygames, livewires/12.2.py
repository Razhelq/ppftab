# Simos says type of game
# Player needs to repeat different combinations of colors and sounds

#  Just began. Not finished

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
        self.delay = 100
        self.level = 3

    def change(self):
        new_butt = New_Button(game = self.game,
                              x = self.x,
                              y = self.y,
                              color = self.color)
        
        games.screen.add(new_butt)


    def update(self):

        self.check_on()

    def check_on(self):
        new_buttons = []
         
        if self.delay > 0:
            self.delay -= 1
        else:
            random_button = Game.Buttons[random.randrange(5)]
            new_buttons.append(random_button)
            random_button.change()
            self.delay += 100
            self.level -= 1            
        

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
  
    
    
    LIFETIME = 40
    
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
    Buttons = []
    
    def __init__(self):
        self.level = 0

        self.sound = games.load_sound("poziom.wav")

        self.score = games.Text(value = 0,
                               size = 30,
                               color = color.white,
                               top = 5,
                               right = games.screen.width - 10)

        games.screen.add(self.score)

    def play(self):

        wallpaper = games.load_image("db.png", transparent = False)
        games.screen.background = wallpaper

        self.advance()

        games.screen.mainloop()

    def advance(self):

        self.location = 100
        for i in range(5):
            new_button = Button(game = self,
                                x = self.location + 100,
                                y = 240,
                                color = Game.color)
            games.screen.add(new_button)
            self.Buttons.append(new_button)
            self.location += 250
            Game.color += 1         
              
        
def main():
    simon = Game()
    simon.play()

main()
                                                           
                                     

                                    

    
        
                                     
                                    
                                












































                                

        


        
                            
        
    

        
