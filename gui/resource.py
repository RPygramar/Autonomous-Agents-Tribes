import pygame
import math


class Resource:
    def __init__(self, screen, grid, current_pos, color, radius):
        self.pixel_pos = (grid.get_cell_x(current_pos[0]), grid.get_cell_y(current_pos[1]))
        self.screen = screen
        self.color = color
        self.rectSize = radius * 2
        self.rect = pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.rectSize, self.rectSize)
        self.rect.center = (self.pixel_pos[0] - radius -1.1, self.pixel_pos[1] - radius -1.1)
    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, int(self.rect.width / 2))

    def __repr__(self):
        return f'Resource - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'



