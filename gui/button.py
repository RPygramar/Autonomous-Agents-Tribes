import pygame
import pygame_gui

class Button:
    def __init__(self, screen, x, y, width, height, text, button_color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 50)
        self.action = action
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
