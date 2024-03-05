import pygame


class GUI:

    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.__cell_size = 10
        self.__screen_width = 900
        self.__screen_height = 900
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        self.bg_color = (201, 193, 181)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("CS-AI")

    def get_cell_size(self):
        return self.__cell_size

    def get_screen_width(self):
        return self.__screen_width

    def get_screen_height(self):
        return self.__screen_height

    def get_screen(self):
        return self.__screen
