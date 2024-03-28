import pygame
import random

from agents.agent import Agent
from resources.resource_algorithm import Resource
from game.grid import Grid
from gui.gui import GUI


class Game:
    def __init__(self):
        # Init interface
        self.gui = GUI()
        self.grid = Grid(self.gui)
        self.grid.load_map()
        self.agent = Agent(self.gui.get_screen(), self.grid, current_pos=(1, 3), color=(100, 100, 100), radius=5)
        self.resource = Resource(self.gui.get_screen(), self.grid, (random.randint(0,89), random.randint(0,89)), color=(0,128,0), radius=5)

        # Init variables for game running
        self.simulating = True
        self.game_running = True

    def run(self):
        while self.game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            # Simulation Running Screen
            if self.simulating:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.agent.move_up()
                    elif event.key == pygame.K_s:
                        self.agent.move_down()
                    elif event.key == pygame.K_d:
                        self.agent.move_right()
                    elif event.key == pygame.K_a:
                        self.agent.move_left()

                # Fill background color
                self.gui.get_screen().fill(self.gui.bg_color)    

                # Update graphic components
                self.update()
            
            # Main Menu Screen
            else:
                self.gui.get_screen().fill((212,175,55)) 
                
            
            # Display    
            pygame.display.flip()
            self.gui.clock.tick(60)

    def update(self):
        self.resource.draw()
        self.agent.draw()
        self.update_pos()

    def update_pos(self):
        self.agent.rect.x, self.agent.rect.y = self.grid.check_move(self.agent.current_pos, self.agent.new_pos, self.agent)
