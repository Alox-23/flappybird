import pygame

class PIPE:
    def __init__(self, game, pos, pipe_gap_y = 200):
        self.game = game
        self.pipe_gap_y = pipe_gap_y

        self.image = pygame.image.load("assets/flappy-bird-assets/sprites/pipe-red.png")
        self.image = pygame.transform.flip(self.image, False, True)
        self.image2 = pygame.image.load("assets/flappy-bird-assets/sprites/pipe-green.png")
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()

        self.rect.topleft = (pos[0],  pos[1]-self.image.get_height()-self.pipe_gap_y/2)

        self.rect2.topleft = (pos[0], pos[1]+self.pipe_gap_y/2)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.game.screen.blit(self.image2, self.rect2)

    def update(self):
        self.rect.x -= self.game.dificulty
        self.rect2.x -= self.game.dificulty