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
        # self.arrow_vertices = [(((self.rect.x+self.grid.get_cell_size())),self.rect.y+self.grid.get_cell_size()),
        #                        (self.rect.x,self.rect.y+self.grid.get_cell_size()//2),
        #                        ((self.rect.x*2+self.grid.get_cell_size())//2,self.rect.y),
        #                        (self.rect.x+self.grid.get_cell_size(),self.rect.y+self.grid.get_cell_size()//2),                                                           
        #                         ((self.rect.x),self.rect.y+self.grid.get_cell_size())
        #                         ]  
        
        self.arrow_vertices = [(((self.rect.x+self.grid.get_cell_size())),self.rect.y+self.grid.get_cell_size()),
                               (self.rect.x+self.grid.get_cell_size(),self.rect.y+self.grid.get_cell_size()/2),
                               ((self.rect.x*2+self.grid.get_cell_size())/2,self.rect.y), 
                               (self.rect.x,self.rect.y+self.grid.get_cell_size()/2),          
                                ((self.rect.x),self.rect.y+self.grid.get_cell_size())
                                ]  


                         
        

    def update(self):
        pass

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.arrow_vertices)



