import pygame
from game import Game

WIDTH = 480
HEIGHT = 600
FPS = 60


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, game: Game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.__init_ship_image(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game.surface.get_width() // 2
        self.rect.bottom = self.game.surface.get_height() - 10
        self.game.objects.append(self)
        self.__subscribe_on_events()

    def __init_ship_image(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, self.__get_ship_size())

    def __get_ship_size(self) -> tuple:
        return self.game.surface.get_width() // 10, \
               self.game.surface.get_height() // 10

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def __subscribe_on_events(self):
        self.moving_left = False
        self.moving_right = False
        self.game.keydown_handlers[pygame.K_LEFT].append(self.handle_keydown)
        self.game.keydown_handlers[pygame.K_RIGHT].append(self.handle_keydown)
        self.game.keyup_handlers[pygame.K_LEFT].append(self.handle_keyup)
        self.game.keyup_handlers[pygame.K_RIGHT].append(self.handle_keyup)

    def handle_keydown(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        elif key == pygame.K_RIGHT:
            self.moving_right = not self.moving_right

    def handle_keyup(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        elif key == pygame.K_RIGHT:
            self.moving_right = not self.moving_right

    def update(self):
        if self.moving_left:
            self.rect.x -= 5
        elif self.moving_right:
            self.rect.x += 5
