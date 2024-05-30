import pygame
import math


class House:
    def __init__(self, screen, grid, current_pos, color, area):
        self.pixel_pos = (grid.get_cell_x(current_pos[0]), grid.get_cell_y(current_pos[1]))
        self.grid = grid
        self.screen = screen
        self.__color = color
        self.rectSize = self.grid.get_cell_size()
        self.rect = pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.rectSize, self.rectSize)                                                              
        
        self.house_vertices = [(((self.rect.x+self.grid.get_cell_size())),self.rect.y+self.grid.get_cell_size()),
                               (self.rect.x+self.grid.get_cell_size(),self.rect.y+self.grid.get_cell_size()/2),
                               ((self.rect.x*2+self.grid.get_cell_size())/2,self.rect.y), 
                               (self.rect.x,self.rect.y+self.grid.get_cell_size()/2),          
                                ((self.rect.x),self.rect.y+self.grid.get_cell_size())
                                ]  
        self.size = area

        self.territory_area = pygame.Rect(self.pixel_pos[0]-self.rectSize*self.size, self.pixel_pos[1]-self.rectSize*self.size, self.rectSize*(self.size*2+1), self.rectSize*(self.size*2+1))     

    def update(self):
        pass

    def draw(self):
        pygame.draw.polygon(self.screen, self.set_color('house'), self.house_vertices)
    
    def draw_territory(self):
        pygame.draw.rect(self.screen, self.set_color('territory'), self.territory_area)

    def set_color(self, type=None):
        rgb = list(self.__color)
        if type == 'house':
            for value in range(len(self.__color)):
                new_value = max(0, min(255, rgb[value] - 30))
                rgb[value] = new_value
            return tuple(rgb)
        else:
            for value in range(len(self.__color)):
                new_value = max(0, min(255, rgb[value] + 80))
                rgb[value] = new_value
            return tuple(rgb)




