# Simplified classic Pong for 1 player.

from livewires import games, color

games.init(screen_width = 630, screen_height = 400, fps = 50)

class Ball(games.Sprite):

    ball_image = games.load_image("bb.png")
    
    def __init__(self):
        super(Ball, self).__init__(image = Ball.ball_image,
                                   x = games.screen.width/2,
                                   y = 20,
                                   dx = 1,
                                   dy = 1)

        self.score = games.Text(value = 0,
                                size = 25,
                                color = color.black,
                                top = 5,
                                right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        elif self.top < 0:
            self.dy = -self.dy
        elif self.bottom > games.screen.height:
            self.destroy()
            self.end_game()
            
        self.check_collision()

    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 50,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
            
        games.screen.add(end_message)

    def check_collision(self):
        for ball in self.overlapping_sprites:
            self.dy = -self.dy
            self.score.value += 10            
            self.dx *= 1.2
            self.dy *= 1.2

class Player(games.Sprite):

    player_image = games.load_image("the_lightsaber.jpg")

    def __init__(self):
        super(Player, self).__init__(image = Player.player_image,
                                     y = games.screen.height - 10,
                                     x = games.mouse.x)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        elif self.right > games.screen.width:
            self.right = games.screen.width

def main():
    court = games.load_image("the_court.jpg", transparent = False)
    games.screen.background = court
    
    basketball = Ball()
    player = Player()
    games.screen.add(basketball)
    games.screen.add(player)
    
    games.mouse.is_visible = False
    games.screen.event_gra = True
    games.screen.mainloop()

main()
    

    
            
            
