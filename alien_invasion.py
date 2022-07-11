import sys
import pygame

from settings import Settings
from strings import Strings
from vectors.ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.strings = Strings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.strings.caption)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for e in pygame.event.get():
                if (e.type == pygame.QUIT):
                    sys.exit()
            self.screen.fill(color=self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
