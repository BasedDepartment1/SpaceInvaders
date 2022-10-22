import pygame


WIDTH = 480
HEIGHT = 640
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    background_image = pygame.image.load('important file.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    while True:
        screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
