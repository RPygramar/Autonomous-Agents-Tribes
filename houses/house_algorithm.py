from gui.house import House

class House_Algo(House):
    def __init__(self, screen, grid, current_pos, color, tribe):
        super().__init__(screen, grid, current_pos, color)
        self.__current_pos = current_pos
        self.new_pos = current_pos
        self.screen = screen
        self.grid = grid

        self.health = 100
        self.__tribe = tribe

    def get_x(self) -> int:
        return self.current_pos[0]

    def get_y(self) -> int:
        return self.current_pos[1]
    
    def get_current_pos(self) -> tuple:
        return self.__current_pos
    
    def set_tribe(self ,tribe) -> None:
        self.__tribe = tribe

    def get_tribe(self) -> str:
        return self.__tribe
    
    def __repr__(self):
        return f'House - Tribe: {self.get_tribe()} - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'