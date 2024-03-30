import pygame
import math


class Resource:
    def __init__(self, screen, grid, current_pos, color, radius):
        self.pixel_pos = (grid.get_cell_x(current_pos[0]), grid.get_cell_y(current_pos[1]))
        self.grid = grid
        self.screen = screen
        self.color = color
        self.rectSize = 10
        self.rect = pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.rectSize, self.rectSize)
        self.__is_drawing = True
        self.triangle_vertices = [(self.rect.x,self.rect.y+self.grid.get_cell_size()),
                                 (self.rect.x+self.grid.get_cell_size(),self.rect.y+self.grid.get_cell_size()),
                                 ((self.rect.x*2+self.grid.get_cell_size())//2,self.rect.y)]

    def update(self):
        pass

    def draw(self):
        if self.__is_drawing:
            pygame.draw.polygon(self.screen, self.color, self.triangle_vertices)

    def __repr__(self):
        return f'Resource - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'
    
    def get_drawing(self):
        return self.__is_drawing
    
    def set_drawing(self, boolean):
        self.__is_drawing = boolean



