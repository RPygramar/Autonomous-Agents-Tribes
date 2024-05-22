from gui.ball import Ball
from algorithm import A_star
import random
import math
import time
import pygame

class Agent(Ball):
    def __init__(self, screen, grid, current_pos, color, radius, tribe_name, resource_limit = 10, attack = 10, health = 100):
        super().__init__(screen, grid, current_pos, color, radius)
        self.__current_pos = current_pos
        self.new_pos = None
        self.screen = screen
        self.grid = grid

        self.health = health
        self.attack_power = attack
        self.__resources = 0
        self.__tribe_name = tribe_name
        self.__resources_limit = resource_limit
        self.actions = {"movement": ['move_up', 'move_down', 'move_left', 'move_right','move_Astar(resources)'],
                        "interaction": ['grab_from_house', 'put_from_house', 'build_house']
                        }
        
        # Callbacks
        self.__on_build_house = None
        self.__on_grab_from_house = None
        self.__on_put_in_house = None

        self.__size = 1
        self.attack_area = None 

    def draw_attack_area(self):
        self.attack_area = pygame.Rect(self.grid.get_cell_x(self.__current_pos[0])-self.rectSize*self.__size, self.grid.get_cell_x(self.__current_pos[1])-self.rectSize*self.__size, self.rectSize*(self.__size*2+1), self.rectSize*(self.__size*2+1))
    
    def get_x(self):
        return self.__current_pos[0]

    def get_y(self):
        return self.__current_pos[1]

    def get_current_pos(self) -> tuple:
        return self.__current_pos

    # ACTION
    def move_Astar(self, list_resources: list) -> None:
        if list_resources:
            path = self.__a_star(list_resources)
            if path:
                for position, next_position in zip(path, path[1:]):
                    if self.grid.entity_grid[next_position[0]][next_position[1]] == 0:
                        self.new_pos = next_position
                        if self.__current_pos[0] < next_position[0]:
                            self.move_right()
                        elif self.__current_pos[0] > next_position[0]:
                            self.move_left()
                        if self.__current_pos[1] < next_position[1]:
                            self.move_down()
                        elif self.__current_pos[1] > next_position[1]:
                            self.move_up()
                        self.rect.x, self.rect.y = self.grid.check_move(self.get_current_pos(), self.new_pos, self)
            # else:
            #     self.build_house(self.__resources_limit)
                    
            
    def move_up(self):
        if self.__current_pos[1] > 0:
            self.__current_pos = (self.__current_pos[0], self.__current_pos[1] - 1)

    def move_down(self):
        if self.__current_pos[1] < (self.screen.get_height() - 1 * self.grid.get_cell_size()) / self.grid.get_cell_size():
            self.__current_pos = (self.__current_pos[0], self.__current_pos[1] + 1)

    def move_left(self):
        if self.__current_pos[0] > 0:
            self.__current_pos = (self.__current_pos[0] - 1, self.__current_pos[1])

    def move_right(self):
        if self.__current_pos[0] < (self.screen.get_width() - 1 * self.grid.get_cell_size()) / self.grid.get_cell_size():
            self.__current_pos = (self.__current_pos[0] + 1, self.__current_pos[1])

    # Update current position to new position (if a move is possible)
    def update_current_pos(self, pos):
        self.__current_pos = pos

    # Update new position to current position (if a move is not possible)
    def update_new_pos(self, pos):
        self.new_pos = pos

    def take_damage(self, damage):
        self.health -= damage
    
    def do_damage(self):
        return self.attack_power

    def get_resources(self):
        return self.__resources
    
    def add_resources(self, resource):
        if not self.is_resources_limit() and (self.__resources + resource <= self.__resources_limit):
            self.__resources += resource

    def build_house(self, house_price):
        if self.__resources >= house_price and self.__on_build_house:
            self.__on_build_house(self)
            self.__resources -= house_price

    def trade_from_house(self, resources):
        self.__resources += resources

    def get_tribe_name(self) -> str:
        return self.__tribe_name
    
    def set_tribe_name(self, tribe_name : str) -> None:
        self.__tribe_name = tribe_name

    def get_limit_resources(self) -> int:
        return self.__resources_limit

    def is_resources_limit(self):
        return self.__resources >= self.__resources_limit
    
    def get_stats(self):
        return (self.health, self.attack)

    def __a_star(self, list_resources):
        def euclidean_distance(pos1, pos2):
            """Calculate the Euclidean distance between two positions."""
            x1, y1 = pos1
            x2, y2 = pos2
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        """Find the closest resource position to the agent."""
        min_distance = float('inf')
        closest_pos = None
        
        for resource in list_resources:
            distance = euclidean_distance(self.get_current_pos(), resource.get_current_pos())
            if distance < min_distance:
                min_distance = distance
                closest_pos = resource.get_current_pos()

        return A_star.A_STAR(self.grid.entity_grid ,self.get_current_pos(), closest_pos)

    def run_agent(self, resources):
        random_movement = "move_Astar"
        random_interaction = random.choice(self.actions['interaction'])
        exec(f'self.{random_movement}(resources)')
        self.draw_attack_area()
        if random_interaction == 'build_house':
            self.build_house(self.__resources_limit)
        elif random_interaction == 'grab_from_house':
            self.__on_grab_from_house()
        elif random_interaction == 'put_from_house':
            self.__on_put_in_house()

    def set_on_build_house_callback(self, callback):
        self.__on_build_house = callback

    def set_on_grab_from_house(self, callback):
        self.__on_grab_from_house = callback

    def set_on_put_in_house(self, callback):
        self.__on_put_in_house = callback

    def __repr__(self):
        return f'Agent {self.get_tribe_name()} - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'