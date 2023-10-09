import pygame as pg
from settings import *
from fighter import Fighter

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.FPS = 60
        pg.display.set_caption("Fighters")
        self.display = pg.display.set_mode((screen_W, screen_H))
        self.bg = pg.image.load(background_1).convert_alpha()
        self.Fighter1 = Fighter(1280/4, 720/2)
        self.Fighter2 = Fighter(1280/1.5, 720/2)
    
    def draw_background(self):
        trans_img = pg.transform.scale(self.bg, (screen_W, screen_H))
        self.display.blit(trans_img, (0,0))

    def draw_life(self, life, x, y):
        tamanho = life/100
        pg.draw.rect(self.display, Branco, (x-1.5, y-1.5, 402, 32))
        pg.draw.rect(self.display, Vermelho, (x, y, 400, 30))
        pg.draw.rect(self.display, Amarelo, (x, y, 400*tamanho, 30))

    def update(self):
        pg.display.update()

    def run(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            self.draw_background()
            self.draw_life(self.Fighter1.saude, 20, 20)
            self.draw_life(self.Fighter2.saude, 580, 20)

            self.Fighter1.move(self.display, self.Fighter2)
            self.Fighter2.move(self.display, self.Fighter1)

            self.Fighter1.draw(self.display)
            self.Fighter2.draw(self.display)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.update()
        pg.quit()