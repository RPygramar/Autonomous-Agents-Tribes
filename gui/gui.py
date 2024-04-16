import pygame
import pygame_gui

class GUI:

    def __init__(self):
        '''Inicializa o pygame'''
        pygame.init()
        pygame.display.init()
        self.__cell_size = 10
        self.__screen_width = 900
        self.__screen_height = 900
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        self.bg_color = (201, 193, 181)
        self.clock = pygame.time.Clock()
        self.__manager = pygame_gui.UIManager((self.__screen_width, self.__screen_height),theme_path='gui/styles.json')
        pygame.display.set_caption("Autonomous-Agents-Tribes")

    def get_cell_size(self):
        return self.__cell_size

    def get_screen_width(self):
        return self.__screen_width

    def get_screen_height(self):
        return self.__screen_height

    def get_screen(self):
        return self.__screen
    
    def get_manager(self):
        return self.__manager

    def draw_button(self):
        self.start_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2)-(self.get_screen_height()//4)), (300, 75)),
                    text='START',
                    manager=self.__manager
                )
    
    def draw_slider_resources(self):
        self.slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2)),(300, 20)),
                                               value_range=(0,8100),
                                               start_value=10,
                                               manager=self.__manager
                                               )
        
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 2 - 50), (300, 20)),
            text="Resources",
            manager=self.__manager
        )

        self.value_resources = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 2), (100, 20)),
            text=f"Value: {self.slider.current_value}",  # Initial text
            manager=self.__manager
        )