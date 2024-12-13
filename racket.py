from abc import ABC, abstractmethod
import config
import pygame
import math

class Racket(ABC, pygame.sprite.Sprite):
    width = 40
    height = 200
    speed = 4
    @abstractmethod
    def __init__(
            self, 
            center_x: int,
            game
    ):
        super().__init__()
        self.center_x = center_x
        self.color = config.WHITE
        self.speed = Racket.speed
        self.rect = pygame.Rect(0, 0, Racket.width,  Racket.height)
        self.game = game
        self.goto_start()

    def goto_start(self):
        self.rect.centerx = self.center_x
        self.rect.centery = self.game.window_height // 2

    def collide_borders(self):
        if self.rect.bottom > self.game.window_height:
            self.rect.bottom = self.game.window_height
        elif self.rect.top < 0:
            self.rect.top = 0

    def render(self):
        '''рисует ракетку'''
        pygame.draw.rect(self.game.screen, self.color, self.rect, 0)

    def update(self):
        self.collide_borders()
        self.move()


class RacketAuto(Racket):
    def __init__(self, center_x, game):
        super().__init__(center_x, game)
        self.delay = 10
        self.last_move = pygame.time.get_ticks()

    def move(self):
        if pygame.time.get_ticks() - self.last_move >= self.delay:
            if self.game.ball.rect.centery < self.rect.centery:
                self.rect.centery -= self.speed
            elif self.game.ball.rect.centery > self.rect.centery:
                self.rect.centery += self.speed
            self.last_move = pygame.time.get_ticks()
    

class RacketManual(Racket):
    def __init__(self, center_x, key_up, key_down, game):
        super().__init__(center_x, game)
        self.key_up = key_up
        self.key_down = key_down

    def move(self):
        if self.game.keys_pressed[self.key_down]:
            self.rect.y += self.speed
        elif self.game.keys_pressed[self.key_up]:
            self.rect.y -= self.speed