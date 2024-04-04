from gui.ball import Ball


class Agent(Ball):
    def __init__(self, screen, grid, current_pos, color, radius, tribe_name):
        super().__init__(screen, grid, current_pos, color, radius)
        self.__current_pos = current_pos
        self.new_pos = current_pos
        self.screen = screen
        self.grid = grid
        self.health = 100
        self.__resourses = 0
        self.__tribe_name = tribe_name

    def get_x(self):
        return self.__current_pos[0]

    def get_y(self):
        return self.__current_pos[1]

    def get_current_pos(self) -> tuple:
        return self.__current_pos

    def move_up(self):
        if self.new_pos[1] > 0:
            self.new_pos = (self.new_pos[0], self.new_pos[1] - 1)

    def move_down(self):
        if self.new_pos[1] < (self.screen.get_height() - 2 * self.grid.get_cell_size()) / self.grid.get_cell_size():
            self.new_pos = (self.new_pos[0], self.new_pos[1] + 1)

    def move_left(self):
        if self.new_pos[0] > 0:
            self.new_pos = (self.new_pos[0] - 1, self.new_pos[1])

    def move_right(self):
        if self.new_pos[0] < (self.screen.get_width() - 2 * self.grid.get_cell_size()) / self.grid.get_cell_size():
            self.new_pos = (self.new_pos[0] + 1, self.new_pos[1])

    # Update current position to new position (if a move is possible)
    def update_current_pos(self):
        self.__current_pos = self.new_pos

    # Update new position to current position (if a move is not possible)
    def update_new_pos(self):
        self.new_pos = self.__current_pos

    def take_damage(self):
        self.health -= 10

    def get_resources(self):
        return self.__resourses
    
    def add_resources(self, resource):
        self.__resourses += resource

    def get_tribe_name(self) -> str:
        return self.__tribe_name
    
    def set_tribe_name(self, tribe_name : str) -> None:
        self.__tribe_name = tribe_name

    def __repr__(self):
        return f'Agent - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'