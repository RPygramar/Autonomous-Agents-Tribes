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
        self.__color = color

        self.__full_health = health
        self.health = health
        self.attack_power = attack
        self.__resources = 0
        self.__tribe_name = tribe_name
        self.__resources_limit = resource_limit
        self.__confidence = random.randint(0,20)
        self.virtual_confidence = 0
        
        self.call_help = False
        # Callbacks
        self.__on_build_house = None
        self.__on_grab_from_house = None
        self.__on_put_in_house = None

        self.__size_attack = 1
        self.__size_call = 8
        self.attack_area = pygame.Rect(self.grid.get_cell_x(self.__current_pos[0])-self.rectSize*self.__size_attack, self.grid.get_cell_x(self.__current_pos[1])-self.rectSize*self.__size_attack, self.rectSize*(self.__size_attack*2+1), self.rectSize*(self.__size_attack*2+1))
        self.call_area = pygame.Rect(self.grid.get_cell_x(self.__current_pos[0])-self.rectSize*self.__size_call, self.grid.get_cell_x(self.__current_pos[1])-self.rectSize*self.__size_call, self.rectSize*(self.__size_call*2+1), self.rectSize*(self.__size_call*2+1))


        self.acasalar = False

    def draw_areas(self):
        self.attack_area = pygame.Rect(self.grid.get_cell_x(self.__current_pos[0])-self.rectSize*self.__size_attack, self.grid.get_cell_x(self.__current_pos[1])-self.rectSize*self.__size_attack, self.rectSize*(self.__size_attack*2+1), self.rectSize*(self.__size_attack*2+1))
        self.call_area = pygame.Rect(self.grid.get_cell_x(self.__current_pos[0])-self.rectSize*self.__size_call, self.grid.get_cell_x(self.__current_pos[1])-self.rectSize*self.__size_call, self.rectSize*(self.__size_call*2+1), self.rectSize*(self.__size_call*2+1))

    def get_x(self):
        return self.__current_pos[0]

    def get_y(self):
        return self.__current_pos[1]

    def get_current_pos(self) -> tuple:
        return self.__current_pos

    def get_color(self) -> tuple:
        return self.__color
    
    def get_confidence(self):
        return self.__confidence
    
    def set_confidence(self, confidence):
        if confidence > 20: confidence = 20
        elif confidence < 0: confidence = 0
        self.__confidence = confidence
    
    def get_full_health(self):
        return self.__confidence

    def clear_path(self):
        self.grid.entity_grid[self.__current_pos[0]][self.__current_pos[1]] = 0
        self.grid.entity_grid[self.new_pos[0]][self.new_pos[1]] = 0

    # ACTION
    def move_Astar(self, list: list) -> None:
        if list:
            path = self.__a_star(list)
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

    def confident_decision(self):
        if self.health >= self.__full_health//2 and (self.get_confidence()+self.virtual_confidence)>10:
            self.call_help = False
            return True
        else:
            return False

    def take_damage(self, damage):
        self.health -= damage
    
    def do_damage(self):
        return self.attack_power

    def get_resources(self):
        return self.__resources
    
    def set_resources(self, amount):
        self.__resources = amount

    def add_resources(self, resource):
        if not self.is_resources_limit() and (self.__resources + resource <= self.__resources_limit):
            self.__resources += resource

    def build_house(self, house_price):
        if self.__resources >= house_price:
            self.__on_build_house(self)

    def put_in_house(self, house):
        if house.get_storage() == house.get_storage_limit():
            pass
        else:
            if self.__on_put_in_house:
                self.__on_put_in_house()

    def attack_house(self, house : object):
        if self.confident_decision():    
            self.move_Astar([house])

    def defend_house(self, enemy_pos):
        if self.confident_decision():
            self.move_Astar([enemy_pos])
 
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

    def __a_star(self, list):
        def euclidean_distance(pos1, pos2):
            """Calculate the Euclidean distance between two positions."""
            x1, y1 = pos1
            x2, y2 = pos2
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        """Find the closest resource position to the agent."""
        min_distance = float('inf')
        closest_pos = None
        
        for pos in list:
            distance = euclidean_distance(self.get_current_pos(), pos.get_current_pos())
            if distance < min_distance:
                min_distance = distance
                closest_pos = pos.get_current_pos()

        return A_star.A_STAR(self.grid.entity_grid ,self.get_current_pos(), closest_pos)

    def colliding_with_house_territory(self, house_list : object):
        for house in house_list:
            if house.territory_area.colliderect(self.rect):
                return house
        return False

    def check_for_help(self, team_agents):
        self.virtual_confidence = 0
        a = None
        for agent in team_agents:
            if agent != self and agent.call_help and self.call_area.colliderect(agent.call_area):
                a = agent
                self.virtual_confidence += 3
                agent.call_help = False
        if a:
            self.move_Astar([a])

    def check_need_heal(self):
        if self.health < self.__full_health//4: return True
        else: return False

    def run_agent(self, resources, houses, team_agents):
        # move_Astar -> Resources
        # build_house -> Constroi uma casa
        # grab_from_house -> Retira recursos de uma casa
        # put_from_house -> Repõe recursos em uma casa
        self.draw_areas()
        if self.confident_decision():
            self.check_for_help(team_agents)
        if self.get_resources() < self.get_limit_resources():
            self.move_Astar(resources)
        elif self.get_resources() >= self.get_limit_resources():
            house = self.colliding_with_house_territory(houses)
            if house:
                self.move_Astar([house])
                self.put_in_house(house)
            else:
                self.build_house(self.__resources_limit)

    def set_on_build_house_callback(self, callback):
        self.__on_build_house = callback

    def set_on_grab_from_house(self, callback):
        self.__on_grab_from_house = callback

    def set_on_put_in_house(self, callback):
        self.__on_put_in_house = callback

    def __repr__(self):
        return f'Agent {self.get_tribe_name()} - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'