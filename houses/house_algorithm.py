from gui.house import House

class House_Algo(House):
    def __init__(self, screen, grid, current_pos, color, tribe : str = 'grey', storage : str = 0, storage_limit : int = 50):
        super().__init__(screen, grid, current_pos, color)
        self.__current_pos = current_pos
        self.new_pos = current_pos
        self.screen = screen
        self.grid = grid

        self.health = 100
        self.__tribe = tribe
        self.__storage = storage

        self.__storage_limit = storage_limit

    def get_x(self) -> int:
        return self.current_pos[0]

    def get_y(self) -> int:
        return self.current_pos[1]
    
    def get_current_pos(self) -> tuple:
        return self.__current_pos
    
    def set_tribe(self ,tribe : str) -> None:
        self.__tribe = tribe

    def get_tribe(self) -> str:
        return self.__tribe
    
    def get_storage(self) -> int:
        return self.__storage
    
    def add_resources_to_storage(self, resources : int) -> int:
        if (self.__storage + resources) <= self.__storage_limit:
            self.__storage += resources
            return - resources
        else:
            difference = self.__storage_limit - self.__storage  
            self.__storage = self.__storage_limit
            return - difference
        

    def remove_resources_from_storage(self, quantity : int, agent_resources : int) -> int:
        if (self.__storage - quantity) >= 0:
            difference = (quantity - agent_resources)
            self.__storage -= difference
            return difference
        else:
            difference = self.__storage
            self.__storage = 0
            return difference

    
    def __repr__(self):
        return f'House - Tribe: {self.get_tribe()} \n Storage: {self.get_storage()} \n Position - x: {self.pixel_pos[0]} | y: {self.pixel_pos[1]}'