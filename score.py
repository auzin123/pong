import config
import pygame

class Score:
    '''табло для показа счета игрока'''

    def __init__(self, center_x: int, center_y: int, game):
        self.center_x = center_x
        self.center_y = center_y
        self.value = 0
        self.color = config.WHITE
        self.size = 100
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(str(self.value), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.game = game

    def render(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(str(self.value), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y