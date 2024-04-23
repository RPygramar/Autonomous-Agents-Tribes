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

    def create_main_menu(self):
        self.__draw_start_button()
        self.__draw_options_button()
        self.__draw_quit_button()

    def create_options_menu(self):
        self.__draw_tribe_option_button()
        self.__draw_agents_option_button()
        self.__draw_resources_option_button()
        self.__draw_houses_option_button()
        self.__draw_back_button()

    def create_tribe_menu(self):
        self.__draw_slider_number_tribes()
        self.__draw_initial_agents_slider()
        self.__draw_back_button()

    def create_agents_menu(self):
        self.__draw_back_button()
        self.__draw_slider_agents_health()
        self.__draw_slider_agents_attack()

    def create_resources_menu(self):
        self.__draw_back_button()
        self.__draw_slider_resources()

    def create_houses_menu(self):
        self.__draw_back_button()
        self.__draw_slider_houses()

    def destroy_main_menu(self):
        self.start_button.kill()
        self.options_button.kill()
        self.quit_button.kill()

    def destroy_options_menu(self):
        self.tribe_button.kill()
        self.agent_button.kill()
        self.houses_button.kill()
        self.back_button.kill()
        self.resources_button.kill()
    
    def destroy_tribe_menu(self):
        self.initial_agents_slider.kill()
        self.value_initial_agents.kill()
        self.slider_initial_agents_label.kill()
        self.tribes_number_slider_label.kill()
        self.tribes_number_slider.kill()
        self.value_number_tribes.kill()
        self.back_button.kill()

    def destroy_agents_menu(self):
        self.back_button.kill()
        self.agents_health_slider_label.kill()
        self.agents_health_slider.kill()
        self.value_agents_health.kill()
        self.agents_attack_slider_label.kill()
        self.agents_attack_slider.kill()
        self.value_agents_attack.kill()

    def destroy_resources_menu(self):
        self.resources_slider.kill()
        self.slider_resources_label.kill()
        self.value_resources.kill()
        self.resources_regeneration_slider.kill()
        self.slider_resources_regeneration_label.kill()
        self.value_resources_regeneration.kill()
        self.back_button.kill()
    
    def destroy_houses_menu(self):
        self.houses_health_slider.kill()
        self.slider_houses_health_label.kill()
        self.value_houses_health.kill()
        self.houses_slider_price.kill()
        self.slider_houses_price_label.kill()
        self.value_houses_price.kill()
        self.houses_max_storage_slider.kill()
        self.value_houses_max_storage.kill()
        self.slider_houses_max_storage_label.kill()
        self.slider_houses_territory_area_label.kill()
        self.value_houses_territory_area.kill()
        self.slider_houses_territory_area.kill()
        self.back_button.kill()

    # START BUTTON
    def __draw_start_button(self):
        self.start_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2)-(self.get_screen_height()//4)), (300, 75)),
                    text='START',
                    manager=self.__manager
                )
    
    # OPTIONS BUTTON
    def __draw_options_button(self):
        self.options_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2 + 100)-(self.get_screen_height()//4)), (300, 75)),
                    text='OPTIONS',
                    manager=self.__manager
                )

    # QUIT BUTTON
    def __draw_quit_button(self):
        self.quit_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2 + 200)-(self.get_screen_height()//4)), (300, 75)),
                    text='QUIT',
                    manager=self.__manager
                )
        
    # BACK BUTTON
    def __draw_back_button(self):
        self.back_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((0,0), (50, 50)),
                    text='<-',
                    manager=self.__manager
                )
        
    # TRIBE BUTTON
    def __draw_tribe_option_button(self):
        self.tribe_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2)-(self.get_screen_height()//4)), (300, 75)),
                    text='TRIBE',
                    manager=self.__manager
                )
    # AGENTS BUTTON
    def __draw_agents_option_button(self):
        self.agent_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2 + 100)-(self.get_screen_height()//4)), (300, 75)),
                    text='AGENTS',
                    manager=self.__manager
                )
    # RESOURCES BUTTON
    def __draw_resources_option_button(self):
        self.resources_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2 + 200)-(self.get_screen_height()//4)), (300, 75)),
                    text='RESOURCES',
                    manager=self.__manager
                )
    # Houses Button
    def __draw_houses_option_button(self):
        self.houses_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//2 + 300)-(self.get_screen_height()//4)), (300, 75)),
                    text='HOUSES',
                    manager=self.__manager
                )
        
    ###############################################################################################################################################
    # TRIBE
    ###############################################################################################################################################
    
    # TRIBE SLIDER
    def __draw_slider_number_tribes(self):
        self.tribes_number_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)-100),(300, 20)),
                                               value_range=(1,4),
                                               start_value=2,
                                               manager=self.__manager
                                               )
        
        self.tribes_number_slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 150), (300, 20)),
            text="Nº Tribes",
            manager=self.__manager
        )

        self.value_number_tribes = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 - 100), (100, 20)),
            text=f"Nº: {self.tribes_number_slider.current_value}",  # Initial text
            manager=self.__manager
        )

    # INITIAL AGENTS PER TRIBE AGENTS
    def __draw_initial_agents_slider(self):
        self.initial_agents_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)),(300, 20)),
                                               value_range=(2,8),
                                               start_value=4,
                                               manager=self.__manager
                                               )
        
        self.slider_initial_agents_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 50), (300, 20)),
            text="Initial Agents per Tribe",
            manager=self.__manager
        )

        self.value_initial_agents = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3), (100, 20)),
            text=f"Value: {self.initial_agents_slider.current_value}",  # Initial text
            manager=self.__manager
        )


    ###############################################################################################################################################
    # AGENTS
    ###############################################################################################################################################

    # AGENTS HEALTH SLIDER
    def __draw_slider_agents_health(self):
        self.agents_health_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)-100),(300, 20)),
                                               value_range=(10,50),
                                               start_value=25,
                                               manager=self.__manager
                                               )
        self.agents_health_slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 150), (300, 20)),
            text="Agents Health",
            manager=self.__manager
        )

        self.value_agents_health = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 - 100), (100, 20)),
            text=f"HP: {self.agents_health_slider.current_value}",  # Initial text
            manager=self.__manager
        )
    
    # AGENTS ATTACK DAMAGE SLIDER
    def __draw_slider_agents_attack(self):
        self.agents_attack_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)),(300, 20)),
                                               value_range=(5,25),
                                               start_value=10,
                                               manager=self.__manager
                                               )
        
        self.agents_attack_slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 50), (300, 20)),
            text="Agents Attack Damage",
            manager=self.__manager
        )

        self.value_agents_attack = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3), (100, 20)),
            text=f"Attack: {self.agents_attack_slider.current_value}",  # Initial text
            manager=self.__manager
        )


    ###############################################################################################################################################
    # Resources
    ###############################################################################################################################################

    # SLIDER RESOURCES
    def __draw_slider_resources(self):
        self.resources_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3 - 100)),(300, 20)),
                                               value_range=(0,6000),
                                               start_value=2000,
                                               manager=self.__manager
                                               )
        
        self.slider_resources_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 150), (300, 20)),
            text="Resources",
            manager=self.__manager
        )

        self.value_resources = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 - 100), (100, 20)),
            text=f"Value: {self.resources_slider.current_value}",  # Initial text
            manager=self.__manager
        )

        self.resources_regeneration_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)),(300, 20)),
                                               value_range=(1,20),
                                               start_value=5,
                                               manager=self.__manager
                                               )
        
        self.slider_resources_regeneration_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 50), (300, 20)),
            text="Seconds for resource regeneration",
            manager=self.__manager
        )

        self.value_resources_regeneration = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3), (100, 20)),
            text=f"Seconds: {self.resources_regeneration_slider.current_value}",  # Initial text
            manager=self.__manager
        )



        ###############################################################################################################################################
        # Houses
        ###############################################################################################################################################

    def __draw_slider_houses(self):
        self.houses_slider_price = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3 - 100)),(300, 20)),
                                            value_range=(1,50),
                                            start_value=10,
                                            manager=self.__manager
                                            )
        
        self.slider_houses_price_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 150), (300, 20)),
            text="House Price",
            manager=self.__manager
        )

        self.value_houses_price = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 - 100), (100, 20)),
            text=f"Price: {self.houses_slider_price.current_value}",  # Initial text
            manager=self.__manager
        )

        self.houses_max_storage_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3)),(300, 20)),
                                            value_range=(10,100),
                                            start_value=50,
                                            manager=self.__manager
                                            )
        
        self.slider_houses_max_storage_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 - 50), (300, 20)),
            text="House Maximum Storage",
            manager=self.__manager
        )

        self.value_houses_max_storage = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3), (100, 20)),
            text=f"Storage: {self.houses_max_storage_slider.current_value}",  # Initial text
            manager=self.__manager
        )

        self.houses_health_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3 + 100)),(300, 20)),
                                            value_range=(10,200),
                                            start_value=100,
                                            manager=self.__manager
                                            )
        
        self.slider_houses_health_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 + 50), (300, 20)),
            text="House Health",
            manager=self.__manager
        )

        self.value_houses_health = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 + 100), (100, 20)),
            text=f"HP: {self.houses_health_slider.current_value}",  # Initial text
            manager=self.__manager
        )

        self.slider_houses_territory_area = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(((self.get_screen_width()//3),(self.get_screen_height()//3 + 200)),(300, 20)),
                                            value_range=(10,200),
                                            start_value=100,
                                            manager=self.__manager
                                            )
        
        self.slider_houses_territory_area_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3, self.get_screen_height() // 3 + 150), (300, 20)),
            text="House Area",
            manager=self.__manager
        )

        self.value_houses_territory_area = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.get_screen_width() // 3 + 25 + 300 + 10, self.get_screen_height() // 3 + 200), (100, 20)),
            text=f"AREA: {self.houses_health_slider.current_value}",  # Initial text
            manager=self.__manager
        )


    ###############################################################################################################################################
    ###############################################################################################################################################

