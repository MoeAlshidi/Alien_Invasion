import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/abood.bmp').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (95, 95))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if(self.rect.right < self.screen_rect.right):
            print('OUT Right')
        elif(self.rect.left > 0):
            print('OUT IN')

    def blitme(self):
        self.screen.blit(self.image, self.rect)
