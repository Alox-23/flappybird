import pygame
import sprite_handler
import pipe
import random

class PIPE_HANDLER(sprite_handler.SPRITE_HANDLER):
    LOWEST_PIPE_Y = 350
    HEIGHTEST_PIPE_Y = 150

    def __init__(self, game):
        self.game = game
        self.sprites = []
        self.pipe_gap_x = 250

        self.add_sprite(pipe.PIPE(self.game, (512,  random.randint(self.HEIGHTEST_PIPE_Y, self.LOWEST_PIPE_Y))))
        for i in range(len(self.sprites)+2):
                self.add_sprite(pipe.PIPE(self.game, (self.sprites[-1].rect.x + self.pipe_gap_x, random.randint(self.HEIGHTEST_PIPE_Y, self.LOWEST_PIPE_Y))))

    def check_death(self):
        for i, sprite in enumerate(self.sprites):
            if sprite.rect.x+sprite.image.get_width() < 0:
                self.remove_sprite(i)

    def check_spawn(self):
        if len(self.sprites) < 4:
            for i in range(len(self.sprites)):
                self.add_sprite(pipe.PIPE(self.game, (self.sprites[-1].rect.x + self.pipe_gap_x, random.randint(self.HEIGHTEST_PIPE_Y, self.LOWEST_PIPE_Y))))
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()

        self.check_death()
        self.check_spawn()