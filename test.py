import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

class Slider:
    def __init__(self, x, y, length, height, min_value, max_value, initial_value):
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

    def draw(self, screen):
        # Draw slider bar
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.length, self.height))
        # Draw slider thumb
        pygame.draw.circle(screen, RED, self.thumb_rect.center, self.thumb_radius)
        # Draw number text
        number_text = self.font.render(f"{self.value:.2f}", True, BLACK)
        screen.blit(number_text, (self.x + self.length + 10, self.y - self.font.get_height() / 2))

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

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slider with Number Counter")

# Create a slider
slider = Slider(100, 300, 400, 10, 0, 100, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle slider events
        slider.handle_event(event)

    # Update slider
    slider.update()

    # Draw everything
    screen.fill(WHITE)
    slider.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
