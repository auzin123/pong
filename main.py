import config # импорт файла config
from ball import Ball # импорт Ball из файла ball
from racket import RacketAuto, RacketManual, Racket # импорт RacketAuto, RacketManual, Racket из файла racket
from score import Score # импорт Score из файла score
import pygame # импорт модуля pygame



class Game: # класс Game
    def __init__(self) -> None: # функция __init__
        pygame.init() # определение pygame
        pygame.mixer.init()
        display_info = pygame.display.Info() # экземпляр класса Info
        self.window_width = display_info.current_w # атрибуты Info (ширина)
        self.window_height = display_info.current_h # атрибуты Info (высота)
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height)
        ) # Игра во весь экран

        self.all_sprites = pygame.sprite.Group()
        
        # левая ракетка
        x_left = self.window_width // 10 # вычисление X левой ракетки
        self.racket_left = RacketManual(
            x_left, 
            pygame.K_w,
            pygame.K_s,
            self
        )

        # правая ракетка
        x_right = self.window_width // 10 * 9 - Racket.width # вычисление X правой ракетки
        self.racket_right = RacketAuto(
            x_right,
            self,
        )
        
        # мяч
        self.ball = Ball(self)

        #левое табло 
        self.score_left = Score(int(self.window_width * 0.25), 100, self)

        #правое табло
        self.score_right = Score(int(self.window_width * 0.75), 100, self)
        
        self.keys_pressed = True
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.main_loop()                   

        pygame.quit()


    def main_loop(self) -> None: # функция main_loop
        while self.is_running:
            '''
            сбор событий
            изменения (обьектов)
            рендер (отрисовка)
            ожидание FPS
            '''
            self.handle_events() # вызов функции handle_events
            self.update() # вызов функции update
            self.render() # вызов функции render
        pygame.quit()

    def handle_events(self) -> None:
        '''обрабатывает события'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
        
        self.keys_pressed = pygame.key.get_pressed()
                    
    def update(self) -> None:
        self.ball.update()
        self.racket_left.update()
        self.racket_right.update()
        self.score_left.update()
        self.score_right.update()

    def render(self):
        '''отрисовывает обьекты на екране'''
        self.screen.fill(config.BLACK)
        self.racket_left.render()
        self.racket_right.render()
        self.ball.render()
        self.score_left.render()
        self.score_right.render()
        pygame.display.flip()


if __name__ == '__main__':
    Game()