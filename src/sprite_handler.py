import pygame

class SPRITE_HANDLER:
    def __init__(self, game):
        self.game = game
        self.sprites = []

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()
        
    def remove_sprite(self, index):
        self.sprites.pop(index)