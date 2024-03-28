from gui.map_object import MapObject


class Grid:
    def __init__(self, gui):
        super().__init__()
        self.__gui = gui
        self.__cell_size = self.__gui.get_cell_size()
        self.entity_grid = []
        self.map_object = MapObject()

    def get_cell_size(self):
        return self.__cell_size

    def get_cell_x(self, pos_x):
        return pos_x * self.__cell_size

    def get_cell_y(self, pos_y):
        return pos_y * self.__cell_size

    def load_map(self):
        with open('map.txt', 'r') as file:
            for line in file:
                entity_list = [int(x) for x in line.split()]
                self.entity_grid.append(entity_list)

    def load_map_object(self):
        for i in range(len(self.entity_grid)):
            for j in range(len(self.entity_grid[i])):
                if self.entity_grid[i][j] != 0 and self.entity_grid[i][j] != 2:
                    self.map_object.draw_object(self.__gui.get_screen(), self.get_cell_x(j), self.get_cell_y(i), self.__cell_size, self.entity_grid[i][j])

    def check_move(self, current_pos, new_pos, agent):
        if self.entity_grid[new_pos[1]][new_pos[0]] == 0:
            self.entity_grid[current_pos[1]][current_pos[0]] = 0
            self.entity_grid[new_pos[1]][new_pos[0]] = 2
            print(f'pos_x: {self.get_cell_x(new_pos[0])}  |  pos_y {self.get_cell_y(new_pos[1])}')
            # for i in range(len(self.entity_grid[0])):
            #     print(self.entity_grid[i])
            agent.update_current_pos()
            return self.get_cell_x(new_pos[0]), self.get_cell_y(new_pos[1])
        agent.update_new_pos()
        return self.get_cell_x(current_pos[0]), self.get_cell_y(current_pos[1])
