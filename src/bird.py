import pygame

class BIRD:
    def __init__(self, game):
        self.game = game
        self.gravity = 0.04
        self.dx, self.dy = 0, 0

        self.image = pygame.image.load("assets/flappy-bird-assets/sprites/yellowbird-downflap.png")
        self.rect = self.image.get_rect()

        self.rect.x = 50

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.dy += self.gravity

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.dy = -self.gravity*5

        self.rect.x += self.dx * self.game.delta_time
        self.rect.y += self.dy * self.game.delta_time

    def check_death(self):
        pass