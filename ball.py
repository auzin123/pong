import config
import pygame
import math

class Ball:
    width = 35
    height = 35
    speed = 2

    def __init__(self, game) -> None:
        self.color = config.WHITE
        self.speed = Ball.speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 75 # углы в градусах
        self.rect = pygame.Rect(0, 0, Ball.width, Ball.height)
        self.game = game
        self.goto_start()
        self.sound = pygame.mixer.Sound(config.SOUNDS_DIR / 'ball.wav')

    def goto_start(self):
        self.rect.centerx = self.game.window_width // 2
        self.rect.centery = self.game.window_height // 2

    def move(self) -> None:
        self.velocity_x = math.cos(math.radians(self.angle - 90))
        self.velocity_y = math.sin(math.radians(self.angle - 90))
        self.rect.x += self.velocity_x * self.speed
        self.rect.y += self.velocity_y * self.speed

    def collide_barders(self) -> None:
        '''столкновение с экраном'''
        if self.rect.top <= 0:
            self.angle *= -1
            self.angle += 180
            self.sound.play()
        elif self.rect.bottom >= self.game.window_height:
            self.angle *= -1
            self.angle += 180
            self.sound.play()

    def collide_rackets(self):
        '''столкновение с ракетками'''
        if self.rect.colliderect(self.game.racket_left.rect):
            self.angle *= -1
        elif self.rect.colliderect(self.game.racket_right.rect):
            self.angle *= -1
            
    def render(self) -> None:
        pygame.draw.rect(self.game.screen, self.color, self.rect, 0)

    def update(self) -> None:
        self.move()
        self.check_goal()
        self.collide_barders()
        self.collide_rackets()


    def check_goal(self) -> None:
        if self.rect.right >  self.game.window_width:
            self.game.score_left.value += 1
            self.goto_start()
            self.game.racket_left.goto_start()
            self.game.racket_right.goto_start()
        elif self.rect.left < 0:
            self.game.score_right.value += 1
            self.goto_start()
            self.game.racket_left.goto_start()
            self.game.racket_right.goto_start()