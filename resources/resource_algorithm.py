from gui.resource import Resource


class Resource_Algo(Resource):
    def __init__(self, screen, grid, current_pos, color):
        super().__init__(screen, grid, current_pos, color)
        self.current_pos = current_pos
        self.new_pos = current_pos
        self.screen = screen
        self.grid = grid

    def get_x(self):
        return self.current_pos[0]

    def get_y(self):
        return self.current_pos[1]
