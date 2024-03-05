import pygame.image
from pygame.sprite import Sprite, RenderPlain


class MapObject(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wall.png')
        self.rect = self.image.get_rect()
        self.wall_group = RenderPlain()

    def draw_object(self, screen, x, y, size, object_type):
        if object_type == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/wall.png'), (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)
        self.wall_group.add(self)
        self.wall_group.draw(screen)

