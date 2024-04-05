import pygame
import math


class House:
    def __init__(self, screen, grid, current_pos, color):
        self.pixel_pos = (grid.get_cell_x(current_pos[0]), grid.get_cell_y(current_pos[1]))
        self.grid = grid
        self.screen = screen
        self.color = color
        self.rectSize = self.grid.get_cell_size()
        self.rect = pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.rectSize, self.rectSize)                                                              
        
        self.house_vertices = [(((self.rect.x+self.grid.get_cell_size())),self.rect.y+self.grid.get_cell_size()),
                               (self.rect.x+self.grid.get_cell_size(),self.rect.y+self.grid.get_cell_size()/2),
                               ((self.rect.x*2+self.grid.get_cell_size())/2,self.rect.y), 
                               (self.rect.x,self.rect.y+self.grid.get_cell_size()/2),          
                                ((self.rect.x),self.rect.y+self.grid.get_cell_size())
                                ]  
        size = 6

        self.territory_area = pygame.Rect(self.pixel_pos[0]-self.rectSize*size, self.pixel_pos[1]-self.rectSize*size, self.rectSize*(size*2+1), self.rectSize*(size*2+1))     

    def update(self):
        pass

    def draw(self):
        pygame.draw.polygon(self.screen, (self.color[0]-30, self.color[1]-30, self.color[2]-30), self.house_vertices)
    
    def draw_territory(self):
        pygame.draw.rect(self.screen, (self.color[0]+60, self.color[1]+60, self.color[2]+60), self.territory_area)




