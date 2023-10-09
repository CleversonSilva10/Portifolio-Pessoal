import pygame as pg
from settings import *

class Fighter():
    def __init__(self, x, y):
        self.rect = pg.Rect((x, y, 80, 180))
        self.velocidadey = 0
        self.pulo = False
        self.ataque = 0
        self.ataque_ativo = False
        self.saude = 100
    
    def draw(self, tela):
        pg.draw.rect(tela, (255, 0, 0), self.rect)
    
    def Ataque(self, tela, player_adversario):
        self.ataque_ativo = True
        ataque_rect = pg.Rect(self.rect.centerx, self.rect.y, 2* self.rect.width, self.rect.height)
        if ataque_rect.colliderect(player_adversario.rect):
            self.saude -= 10
            self.ataque_ativo = False

    def move(self, tela, player_adversario):
        speed = 10
        gravidade = 2
        delta_x = 0
        delta_y = 0

        key = pg.key.get_pressed()

        if self.ataque_ativo == False:
            if key[pg.K_a]:
                delta_x = -speed
            elif key[pg.K_d]:
                delta_x = +speed
            elif key[pg.K_w] and self.pulo == False:
                self.velocidadey = -30
                self.pulo = True
            elif key[pg.K_r] or key[pg.K_t]:
                if key[pg.K_r]:
                    self.Ataque(tela, player_adversario)
                    self.ataque = 1
                elif key [pg.K_t]:
                    self.ataque = 2

        self.velocidadey += gravidade
        delta_y += self.velocidadey

        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
        elif self.rect.right + delta_x > screen_W:
            delta_x = screen_W - self.rect.right
        elif self.rect.bottom + delta_y > screen_H - 150:
            self.velocidadey = 0
            self.pulo = False
            delta_y = screen_H - 150 - self.rect.bottom

        self.rect.x += delta_x
        self.rect.y += delta_y