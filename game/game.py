from multiprocessing import Process, Queue
from threading import Thread
import pygame
import pygame_gui
import random
import asyncio

from agents.agent import Agent
from resources.resource_algorithm import Resource_Algo as Resource
from game.tribe import Tribe
from houses.house_algorithm import House_Algo as House 


from game.grid import Grid
from gui.gui import GUI

from gui.plots import Plot


class Game:
    def __init__(self):
        
        # Init interface
        self.gui = GUI()
        self.queue = Queue()
        self.grid = Grid(self.gui)
        self.grid.load_map()

        # Init main menu
        self.gui.create_main_menu()

        # Init variables for game running
        self.mode = 0 # 'menu' = 0, 'options' = 1, 'simulating' = 2, 'tribe' = 3, 'agents' = 4, 'resources' = 5, 'houses' = 6
        self.game_running = True

        # Multi process (Plot)
        self.p = None

        # Resource counter
        self.total_resources = 0

        # Agent List
        self.all_agents_list = []

        # Rules
        self.house_price = 10 # Resources needed to build a house

        # Default Values
        self.total_resources = 6000
        self.agents_per_tribe = 4
        self.regeneration_time = 5000


    def start_matplotlib_process(self):
        self.p = Process(target=Plot().main, args=(self.queue,))
        self.p.start()


    # MÉTODO QUE MANIPULA O JOGO
    def run(self):
        while self.game_running:

            time_delta = self.gui.clock.tick(60) / 1000.0
            
            # Screen da Simulação
            if self.mode == 2:                   
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                        self.p.terminate()

                # Fill background color
                self.gui.get_screen().fill(self.gui.bg_color)    

                # Update aos componentes da simulação
                self.update()

                # Enviar informação para o gráfico
                self.queue.put(self.total_resources)
            
            # Screen do Main Menu
            elif self.mode == 0:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False

                    # Process events for the UIManager
                    self.gui.get_manager().process_events(event)

                    if event.type == pygame.USEREVENT:
                        
                        # Verifica se o botão START foi clicado e se sim inicia a simulação
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.start_button:
                                self.mode = 2
                                self.start_game()
                                self.start_matplotlib_process()
                            elif event.ui_element == self.gui.quit_button:
                                self.game_running = False
                            elif event.ui_element == self.gui.options_button:
                                self.mode = 1

                                # Destroy Components
                                self.gui.destroy_main_menu()

                                # Create Component Option Menu
                                self.gui.create_options_menu()
            # OPTIONS MENU
            elif self.mode == 1:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    self.gui.get_manager().process_events(event)
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.tribe_button:
                                self.mode = 3

                                # Destroy Components
                                self.gui.destroy_options_menu()

                                # Create Component Tribe Option Menu
                                self.gui.create_tribe_menu()
                            elif event.ui_element == self.gui.back_button:
                                self.mode = 0

                                # Destroy Components
                                self.gui.destroy_options_menu()

                                # Create Component Tribe Option Menu
                                self.gui.create_main_menu()
                            elif event.ui_element == self.gui.agent_button:
                                self.mode = 4

                                # Destroy Components
                                self.gui.destroy_options_menu()

                                # Create Component Tribe Option Menu
                                self.gui.create_agents_menu()
                            elif event.ui_element == self.gui.resources_button:
                                self.mode = 5

                                # Destroy Components
                                self.gui.destroy_options_menu()

                                # Create Component Tribe Option Menu
                                self.gui.create_resources_menu()
                            elif event.ui_element == self.gui.houses_button:
                                self.mode = 6

                                # Destroy Components
                                self.gui.destroy_options_menu()

                                # Create Component Tribe Option Menu
                                self.gui.create_houses_menu()
            
            # TRIBE OPTION
            elif self.mode == 3:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    self.gui.get_manager().process_events(event)
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            if event.ui_element == self.gui.tribes_number_slider:
                                self.gui.value_number_tribes.set_text(f"Nº: {event.value:.0f}")
                            elif event.ui_element == self.gui.initial_agents_slider:
                                self.gui.value_initial_agents.set_text(f"Value: {event.value:.0f}")
                                self.agents_per_tribe = int(event.value)
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.back_button:
                                self.mode = 1

                                # Destroy Components
                                self.gui.destroy_tribe_menu()

                                # Create Component Option Menu
                                self.gui.create_options_menu()

            # AGENTS OPTION
            elif self.mode == 4:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    self.gui.get_manager().process_events(event)
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.back_button:
                                self.mode = 1

                                # Destroy Components
                                self.gui.destroy_agents_menu()

                                # Create Component Option Menu
                                self.gui.create_options_menu()
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            if event.ui_element == self.gui.agents_health_slider:
                                self.gui.value_agents_health.set_text(f"HP: {event.value:.0f}")
                            if event.ui_element == self.gui.agents_attack_slider:
                                self.gui.value_agents_attack.set_text(f"Attack: {event.value:.0f}")

            elif self.mode == 5:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    self.gui.get_manager().process_events(event)
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.back_button:
                                self.mode = 1

                                # Destroy Components
                                self.gui.destroy_resources_menu()

                                # Create Component Option Menu
                                self.gui.create_options_menu()
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            if event.ui_element == self.gui.resources_slider:
                                self.gui.value_resources.set_text(f"Value: {event.value:.0f}")
                                self.total_resources = int(event.value)
                            elif event.ui_element == self.gui.resources_regeneration_slider:
                                self.gui.value_resources_regeneration.set_text(f"Seconds: {event.value:.0f}")
                                self.regeneration_time = int(event.value) * 1000

            elif self.mode == 6:
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    self.gui.get_manager().process_events(event)
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.back_button:
                                self.mode = 1

                                # Destroy Components
                                self.gui.destroy_houses_menu()

                                # Create Component Option Menu
                                self.gui.create_options_menu()
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            if event.ui_element == self.gui.houses_slider_price:
                                self.gui.value_houses_price.set_text(f"Price: {event.value:.0f}")
                            elif event.ui_element == self.gui.houses_health_slider:
                                self.gui.value_houses_health.set_text(f"HP: {event.value:.0f}")
                            elif event.ui_element == self.gui.slider_houses_territory_area:
                                self.gui.value_houses_territory_area.set_text(f"AREA: {event.value:.0f}")
                            elif event.ui_element == self.gui.houses_max_storage_slider:
                                self.gui.value_houses_max_storage.set_text(f"Storage: {event.value:.0f}")


            # Display
            self.gui.get_manager().update(time_delta)
            pygame.display.flip()

    def update(self):
        '''Desenha os diferentes objetos para a simulação'''
        
        for house in self.all_houses_list:
            house.draw_territory()

        for house in self.all_houses_list:
            house.draw()

        for resource in self.resources: # Desenhar todos os resources dentro da lista criada após o start
            resource.draw()

        for agent in self.all_agents_list:
            agent.draw()

        for tribe in self.tribes.values():
            print('WILL START TRIBE RUNNING')
            tribe.run_tribe(self.resources)

        self.update_pos()

        self.check_collisions()

    def update_start_menu(self):
        '''Desenha os elementos do Menu Inicial'''
        self.gui.get_manager().draw_ui(self.gui.get_screen())

    def on_build_house(self, agent : object):
        if agent.get_resources() >= self.house_price and not self.is_house_in_position(agent.get_current_pos()):
            house = House(self.gui.get_screen(), self.grid, agent.get_current_pos(), agent.color, tribe= agent.get_tribe_name())
            self.all_houses_list.append(house)
            self.add_house_to_tribe(house.get_tribe(), house)

    def on_put_in_house(self):
        for agent in self.all_agents_list:
            for house in self.all_houses_list:
                if agent.rect.colliderect(house.rect):
                    if agent.get_tribe_name() == house.get_tribe():
                        agent.trade_from_house(house.add_resources_to_storage(agent.get_resources()))

    def on_grab_from_house(self):
        for agent in self.all_agents_list:
            for house in self.all_houses_list:
                if agent.rect.colliderect(house.rect):
                        agent.trade_from_house(house.remove_resources_from_storage(agent.get_limit_resources(),agent.get_resources()))

    def update_pos(self):
        for agent in self.all_agents_list:
            agent.rect.x, agent.rect.y = self.grid.check_move(agent.get_current_pos(), agent.new_pos, agent)

    def add_house_to_tribe(self, tribe : str, house):
        self.tribes[tribe].add_house(house)

    def start_game(self):
        '''Inicia o jogo com os recursos, tribos e tempo de regeneração dos recursos de acordo com o escolhido pelo utilizador'''
        self.resources = []
        positions = [] # Cria-se uma lista vazia para preencher todas as posições com recursos
        iterations = self.total_resources

        # RESOURCES CREATE

        for i in range(int(iterations)): # Popula-se a lista positions com posições aleatórias e distintas
            random_tuple = (random.randint(0,89),random.randint(0,89))
            while random_tuple in positions:
                random_tuple = (random.randint(0,89),random.randint(0,89))
            positions.append(random_tuple)
    
            self.resources.append(Resource(self.gui.get_screen(), self.grid, random_tuple, color=(0,128,0))) # Popula-se a lista resources com as shapes "resource"
            
        del positions # elimina-se a lista para não ocupar memória

        # TRIBE CREATE

        self.tribes = {'grey': Tribe(tribe_name='grey')}

        # AGENT CREATE

        for _ in range(int(self.agents_per_tribe)):
            agent = Agent(self.gui.get_screen(), self.grid, current_pos=(random.randint(0,89), random.randint(0,89)), color=(100, 100, 100), radius=5, tribe_name='grey', resource_limit=self.house_price)
            self.all_agents_list.append(agent)
            self.tribes['grey'].add_agent(agent)

        # HOUSE CREATE

        self.all_houses_list = []

        # print(self.tribes)

        # Callbacks
        for agent in self.all_agents_list:
            agent.set_on_build_house_callback(self.on_build_house)
            agent.set_on_grab_from_house(self.on_grab_from_house)
            agent.set_on_put_in_house(self.on_put_in_house)
        
        # Thread(target=agent.run_agent(self.resources)).start()
        # Process(target=agent.run_agent(self.resources)).start()

    def check_collisions(self):

        # Agent - Resource
        for agent in self.all_agents_list:
            for resourse in self.resources:
                if agent.rect.colliderect(resourse.rect) and not agent.is_resources_limit():
                    self.resources.remove(resourse)
                    self.total_resources -= 1
                    agent.add_resources(1)
                    # print('Tribes: ',self.tribes['grey'].get_total_resources())
                    break

    def is_house_in_position(self, wanted_position) -> bool:
        for h in self.all_houses_list:
            if h.get_current_pos() == wanted_position:
                return True
        return False