import pygame
import bird
import pipe_handler

pygame.init()

class GAME: 
    def __init__(self):
        self.dificulty = 5
        self.screen = pygame.display.set_mode((288, 512))
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("assets/flappy-bird-assets/sprites/background-day.png")
        self.p = bird.BIRD(self)
        self.pipes = pipe_handler.PIPE_HANDLER(self)
    
    def draw_bg(self):
        self.screen.blit(self.background, (0,0))

    def draw(self):
        pygame.display.set_caption("fps: " + str(int(self.clock.get_fps())))
        self.draw_bg()

        self.p.draw()
        self.pipes.draw()

    def update(self):
        self.delta_time = self.clock.tick(60)

        self.p.update()
        self.pipes.update()

    def mainloop(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.draw()

            self.update()

            pygame.display.update()
        
        pygame.quit()


if __name__ == "__main__":
    game = GAME()
    game.mainloop()