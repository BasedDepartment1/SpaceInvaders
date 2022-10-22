from singleton import Singleton
import pygame
import sys
from collections import defaultdict


class Game(metaclass=Singleton):
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):
        self.background_image = pygame.image.load(back_image_filename)
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (width, height))
        self.frame_rate = frame_rate
        self.__init_pygame_components()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.__init_key_handlers()

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def update(self):
        for game_object in self.objects:
            game_object.update()

    def draw(self):
        for game_object in self.objects:
            game_object.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__handle_key_events(event, self.keydown_handlers)
            elif event.type == pygame.KEYUP:
                self.__handle_key_events(event, self.keyup_handlers)
            elif self.__is_mouse_event(event):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def __init_key_handlers(self):
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def __init_pygame_components(self):
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()

    @staticmethod
    def __handle_key_events(event: pygame.event, handlers: defaultdict):
        for handler in handlers[event.key]:
            handler(event.key)

    @staticmethod
    def __is_mouse_event(event: pygame.event) -> bool:
        return event.type in (pygame.MOUSEBUTTONDOWN,
                              pygame.MOUSEBUTTONUP,
                              pygame.MOUSEMOTION)
