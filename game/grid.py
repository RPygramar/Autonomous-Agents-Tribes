class Grid:
    def __init__(self, gui):
        self.__gui = gui
        self.__cell_size = self.__gui.get_cell_size()
        self.entity_grid = []

    def get_cell_size(self): 
        return self.__cell_size

    def get_cell_x(self, pos_x):
        return pos_x * self.__cell_size

    def get_cell_y(self, pos_y):
        return pos_y * self.__cell_size

    def load_map(self): # Inicializa uma grelha com as posições correspondentes ao map.txt
        with open('map.txt', 'r') as file:
            for line in file:
                entity_list = [int(x) for x in line.split()]
                self.entity_grid.append(entity_list)

    # Verifica se a posição está ocupada, 2 para ocupada por um jogador 0 para desocupada
    # Se não estiver ocupada altera a posição do jogador para a pretendida
    # Se estiver ocupada não altera a posição do jogador
    def check_move(self, current_pos, new_pos, agent):
        if self.entity_grid[new_pos[1]][new_pos[0]] == 0:
            self.entity_grid[current_pos[1]][current_pos[0]] = 0
            self.entity_grid[new_pos[1]][new_pos[0]] = 0
            # print(f'pos_x: {self.get_cell_x(new_pos[0])}  |  pos_y {self.get_cell_y(new_pos[1])}')
            agent.update_current_pos()
            return self.get_cell_x(new_pos[0]), self.get_cell_y(new_pos[1])
        agent.update_new_pos()
        return self.get_cell_x(current_pos[0]), self.get_cell_y(current_pos[1])
