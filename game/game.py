import pygame

from agents.agent import Agent
from game.grid import Grid
from gui.gui import GUI


class Game:
    def __init__(self):
        self.gui = GUI()
        self.grid = Grid(self.gui)
        self.grid.load_map()
        self.agent = Agent(self.gui.get_screen(), self.grid, current_pos=(1, 3), color=(100, 100, 100), radius=5, speed=8, angle=-50)
        self.background = pygame.image.load('assets/background.png')

    def run(self):
        game_running = True
        while game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.agent.move_up()
                    elif event.key == pygame.K_s:
                        self.agent.move_down()
                    elif event.key == pygame.K_d:
                        self.agent.move_right()
                    elif event.key == pygame.K_a:
                        self.agent.move_left()

            # Redraw the screen during each pass through the loop
            # self.gui.get_screen().fill())

            # Load map objects
            # self.grid.load_map_object()
            self.gui.get_screen().blit(self.background, (0, 0))

            # Update graphic components
            self.update()

            pygame.display.flip()
            self.gui.clock.tick(60)

    def update(self):
        self.agent.draw()
        self.update_pos()

    def update_pos(self):
        self.agent.rect.x, self.agent.rect.y = self.grid.check_move(self.agent.current_pos, self.agent.new_pos, self.agent)
