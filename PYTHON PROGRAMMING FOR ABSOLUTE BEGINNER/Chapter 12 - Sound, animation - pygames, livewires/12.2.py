# Simos says type of game
# Player needs to repeat different combinations of colors and sounds

#  Just began. Not finished

import math, random
from livewires import games, color

games.init(screen_width = 900, screen_height = 480, fps = 50)

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

    images = {red_light    : games.load_image("red_light.jpg"),
              red_dark     : games.load_image("red_dark.jpg"),
              black_light  : games.load_image("black_light.jpg"),
              black_dark   : games.load_image("black_dark.jpg"),
              green_light  : games.load_image("green_light.jpg"),
              green_dark   : games.load_image("green_dark.png"),
              blue_light   : games.load_image("blue_light.png"),
              blue_dark    : games.load_image("blue_dark.png"),
              yellow_light : games.load_image("yellow_light.png"),
              yellow_dark  : games.load_image("yellow_dark.jpg")}
  
    def __init__(self, game, x, y, color):
        super(Button, self).__init__(image = Button.images[color],
                                     x = x,
                                     y = y)

        self.game = game
        self.color = color      

        
class Game(object):
    color = 0
    
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

        wallpaper = games.load_image("d2.jpg")
        games.screen.background = wallpaper

        self.advance()

        games.screen.mainloop()

    def advance(self):

        self.level += 1
        self.location = 250

        for i in range(6):
            new_button = Button(game = self,
                                x = self.location + 100,
                                y = 220,
                                color = Game.color)
            games.screen.add(new_button)
            Game.color += 1

def main():
    simon = Game()
    simon.play()

main()
                                                           
                                     

                                    

    
        
                                     
                                    
                                












































                                

        


        
                            
        
    

        
