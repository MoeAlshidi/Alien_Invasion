import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullets_color
        self.rect = pygame.Rect(
            0, 0, self.settings.bullets_width, self.settings.bullets_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullets_speed
        self.rect.y = self.y

    def draw_bullets(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
