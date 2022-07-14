
import sys
import pygame
from vectors.bullet import Bullet
from settings import Settings
from strings import Strings
from vectors.alien import Alien
from vectors.bullet import Bullet
from vectors.ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.strings = Strings()
        self.bullets = pygame.sprite.Group()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.strings.caption)
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _move_ship_horizontal(self, direction):
        if(direction == 'Right'):
            self.ship.rect.x += self.settings.ship_speed
        elif(direction == 'Left'):
            self.ship.rect.x -= self.settings.ship_speed

    def _move_ship_vertical(self, direction):
        if(direction == 'Up'):
            self.ship.rect.y -= self.settings.ship_speed
        elif(direction == 'Down'):
            self.ship.rect.y += self.settings.ship_speed

    def _check_events(self):
        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                sys.exit()
            elif (e.type == pygame.KEYDOWN):
                if(e.key == pygame.K_RIGHT):
                    self._move_ship_horizontal('Right')
                elif(e.key == pygame.K_LEFT):
                    self._move_ship_horizontal('Left')
                elif(e.key == pygame.K_UP):
                    self. _move_ship_vertical('Up')
                elif(e.key == pygame.K_DOWN):
                    self. _move_ship_vertical('Down')
                elif(e.key == pygame.K_SPACE):
                    self._fire_bullets()
                elif(e.key == pygame.K_q):
                    sys.exit()

    def _fire_bullets(self):
        if(len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(color=self.settings.bg_color)
        self.ship.blitme()
        for bullets in self.bullets.sprites():
            bullets.draw_bullets()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        space_x = self.settings.screen_width-(2*alien_width)
        num_of_aliens = space_x//(2*alien_width)
        for e in range(num_of_aliens):
            self. _create_aliens(e)

    def _create_aliens(self, e):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width+2*alien_width*e
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def run_game(self):
        while True:
            self. _check_events()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
