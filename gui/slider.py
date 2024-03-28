import pygame

class Slider:
    def __init__(self, screen, x, y, length, height, min_value, max_value, initial_value):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.thumb_radius = height // 2
        self.thumb_rect = pygame.Rect(x, y - self.thumb_radius, height, height)
        self.dragging = False
        self.font = pygame.font.SysFont(None, 32)
        self.screen = screen

    def draw(self):
        # Draw slider bar
        pygame.draw.rect(self.screen, (34, 40, 49), (self.x, self.y, self.length, self.height))
        # Draw slider thumb
        pygame.draw.circle(self.screen, (118, 171, 174), self.thumb_rect.center, self.thumb_radius)
        # Draw number text
        number_text = self.font.render(f"{self.value:.0f}", True, (238, 238, 238))
        self.screen.blit(number_text, (self.x + self.length + 10, self.y - self.font.get_height() / 2))

    def update(self):
        # Update thumb position based on value
        thumb_pos = int((self.value - self.min_value) / (self.max_value - self.min_value) * (self.length - self.thumb_radius * 2)) + self.x
        self.thumb_rect.centerx = thumb_pos + self.thumb_radius

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.thumb_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                # Move thumb with mouse movement
                self.thumb_rect.centerx = min(max(event.pos[0], self.x + self.thumb_radius), self.x + self.length - self.thumb_radius)
                # Update value based on thumb position
                self.value = ((self.thumb_rect.centerx - self.x - self.thumb_radius) / (self.length - self.thumb_radius * 2)) * (self.max_value - self.min_value) + self.min_value
                self.value = min(max(self.value, self.min_value), self.max_value)

    def get_value(self):
        return self.value