import pygame
from game import Game
from spaceship import Spaceship

WIDTH = 480
HEIGHT = 640
FPS = 60


def main():
    pygame.init()
    game = Game('Space Invaders', WIDTH, HEIGHT, 'images/important file.jpg', FPS)
    spaceship = Spaceship('images/ship_002.png', game)
    spaceship.draw(game.surface)
    game.run()


if __name__ == "__main__":
    main()
