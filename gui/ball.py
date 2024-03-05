import pygame
import math


class Ball:
    def __init__(self, screen, grid, current_pos, color, radius, speed, angle=45):
        self.pixel_pos = (grid.get_cell_x(current_pos[0]), grid.get_cell_y(current_pos[1]))
        self.screen = screen
        self.color = color
        self.rectSize = radius * 2
        self.rect = pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.rectSize, self.rectSize)
        self.speed = speed
        self.angle = math.radians(angle)

    def update(self):
        # delta_x = self.speed * math.cos(self.angle)
        # delta_y = self.speed * math.sin(self.angle)
        # self.rect = self.rect.move(delta_x, delta_y)
        #
        # if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
        #     self.angle = math.pi - self.angle
        #
        # if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
        #     self.angle = -self.angle
        pass

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, int(self.rect.width / 2))



