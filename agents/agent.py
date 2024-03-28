from gui.ball import Ball


class Agent(Ball):
    def __init__(self, screen, grid, current_pos, color, radius):
        super().__init__(screen, grid, current_pos, color, radius)
        self.current_pos = current_pos
        self.new_pos = current_pos
        self.screen = screen
        self.grid = grid

    def get_x(self):
        return self.current_pos[0]

    def get_y(self):
        return self.current_pos[1]

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
        self.current_pos = self.new_pos

    # Update new position to current position (if a move is not possible)
    def update_new_pos(self):
        self.new_pos = self.current_pos
