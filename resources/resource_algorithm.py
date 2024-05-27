from gui.resource import Resource
import random
import pygame


class Resource_Algo(Resource):
    def __init__(self, screen, grid, current_pos, color):
        super().__init__(screen, grid, current_pos, color)
        self.current_pos = current_pos
        self.screen = screen
        self.grid = grid
        self.start_time = pygame.time.get_ticks()

    def get_x(self):
        return self.current_pos[0]

    def get_y(self):
        return self.current_pos[1]

    def get_current_pos(self):
        return self.current_pos
        
            
