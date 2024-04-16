from multiprocessing import Process, Queue
import pygame
import pygame_gui
import random

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
        self.gui.draw_button()
        self.gui.draw_slider_resources()

        # Init variables for game running
        self.simulating = False
        self.game_running = True

        # Multi process (Plot)
        self.p = None

        # Resource counter
        self.total_resources = 0

        # Agent List
        self.all_agents_list = []

        # Rules
        self.house_price = 10 # Resources needed to build a house


    def start_matplotlib_process(self):
        self.p = Process(target=Plot().main, args=(self.queue,))
        self.p.start()


    # MÉTODO QUE MANIPULA O JOGO
    def run(self):
        while self.game_running:

            time_delta = self.gui.clock.tick(60) / 1000.0

            # Screen da Simulação
            if self.simulating:                   
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                        self.p.terminate()
                        
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            self.agent.move_up()
                        elif event.key == pygame.K_s:
                            self.agent.move_down()
                        elif event.key == pygame.K_d:
                            self.agent.move_right()
                        elif event.key == pygame.K_a:
                            self.agent.move_left()
                        elif event.key == pygame.K_SPACE:
                            self.agent.move_Astar(list_resources=self.resources)
                        elif event.key == pygame.K_h:
                            if self.agent.get_resources() >= self.house_price and not self.is_house_in_position(self.agent.get_current_pos()):
                                house = House(self.gui.get_screen(), self.grid, self.agent.get_current_pos(), self.agent.color, tribe= self.agent.get_tribe_name())
                                self.all_houses_list.append(house)
                                self.agent.build_house(self.house_price)
                                print(self.agent.get_resources())
                                print(self.all_houses_list)
                                self.add_house_to_tribe(house.get_tribe(), house)
                        elif event.key == pygame.K_p:
                            for agent in self.all_agents_list:
                                for house in self.all_houses_list:
                                    if agent.rect.colliderect(house.rect):
                                        if agent.get_tribe_name() == house.get_tribe():
                                            agent.trade_from_house(house.add_resources_to_storage(agent.get_resources()))
                                            print(house)
                                            print(agent.get_resources())
                        elif event.key == pygame.K_g:
                            for agent in self.all_agents_list:
                                for house in self.all_houses_list:
                                    if agent.rect.colliderect(house.rect):
                                            agent.trade_from_house(house.remove_resources_from_storage(10,agent.get_resources()))
                                            print(house)
                                            print(agent.get_resources())

                # Fill background color
                self.gui.get_screen().fill(self.gui.bg_color)    

                # Update aos componentes da simulação
                self.update()

                # Enviar informação para o gráfico
                self.queue.put(self.total_resources)
            
            # Screen do Main Menu
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False

                    # Process events for the UIManager
                    self.gui.get_manager().process_events(event)

                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            # Update ao valor do slider do Main Menu
                            self.gui.value_resources.set_text(f"Value: {event.value:.0f}")
                            
                        
                        # Verifica se o botão START foi clicado e se sim inicia a simulação
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.start_button:
                                self.total_resources = int(self.gui.slider.current_value)
                                self.simulating = True
                                self.start_game()
                                self.start_matplotlib_process()
                               
                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                
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
            agent.run_agent(self.house_price, self.resources)
            agent.draw()

        self.update_pos()

        self.check_collisions()

    def update_start_menu(self):
        '''Desenha os elementos do Menu Inicial'''
        self.gui.get_manager().draw_ui(self.gui.get_screen())

    def on_build_house(self):
        print('Resources: ',self.agent.get_resources(), 'is_house_in_position? : ', self.is_house_in_position(self.agent.get_current_pos()))
        if self.agent.get_resources() >= self.house_price and not self.is_house_in_position(self.agent.get_current_pos()):
            house = House(self.gui.get_screen(), self.grid, self.agent.get_current_pos(), self.agent.color, tribe= self.agent.get_tribe_name())
            self.all_houses_list.append(house)
            print("Houses:", self.all_houses_list)
            print(self.agent.get_resources())
            #print(self.all_houses_list)
            self.add_house_to_tribe(house.get_tribe(), house)

    def on_put_in_house(self):
        for agent in self.all_agents_list:
            for house in self.all_houses_list:
                if agent.rect.colliderect(house.rect):
                    if agent.get_tribe_name() == house.get_tribe():
                        agent.trade_from_house(house.add_resources_to_storage(agent.get_resources()))
                        print(house)
                        print(agent.get_resources())

    def on_grab_from_house(self):
        for agent in self.all_agents_list:
            for house in self.all_houses_list:
                if agent.rect.colliderect(house.rect):
                        agent.trade_from_house(house.remove_resources_from_storage(agent.get_limit_resources(),agent.get_resources()))
                        print(house)
                        print(agent.get_resources())


    def update_pos(self):
        self.agent.rect.x, self.agent.rect.y = self.grid.check_move(self.agent.get_current_pos(), self.agent.new_pos, self.agent)

    def add_house_to_tribe(self, tribe : str, house):
        self.tribes[tribe].add_house(house)

    def start_game(self):
        '''Inicia o jogo com os recursos, tribos e tempo de regeneração dos recursos de acordo com o escolhido pelo utilizador'''
        self.resources = []
        positions = [] # Cria-se uma lista vazia para preencher todas as posições com recursos
        iterations = self.gui.slider.current_value

        # TEST AGENT
        self.agent = Agent(self.gui.get_screen(), self.grid, current_pos=(1, 3), color=(100, 100, 100), radius=5, tribe_name='grey', resource_limit=self.house_price)

        for i in range(int(iterations)): # Popula-se a lista positions com posições aleatórias e distintas
            random_tuple = (random.randint(0,89),random.randint(0,89))
            while random_tuple in positions:
                random_tuple = (random.randint(0,89),random.randint(0,89))
            positions.append(random_tuple)
    
            self.resources.append(Resource(self.gui.get_screen(), self.grid, random_tuple, color=(0,128,0))) # Popula-se a lista resources com as shapes "resource"
            
        del positions # elimina-se a lista para não ocupar memória

        self.tribes = {'grey': Tribe(tribe_name='grey')}

        self.tribes['grey'].add_agent(self.agent)

        self.all_agents_list.append(self.agent)

        self.all_houses_list = []

        print(self.tribes['grey'])

        # Callbacks
        self.agent.set_on_build_house_callback(self.on_build_house)
        self.agent.set_on_grab_from_house(self.on_grab_from_house)
        self.agent.set_on_put_in_house(self.on_put_in_house)

    def check_collisions(self):

        # Agent - Resource
        for agent in self.all_agents_list:
            for resourse in self.resources:
                if agent.rect.colliderect(resourse.rect) and not agent.is_resources_limit():
                    self.resources.remove(resourse)
                    self.total_resources -= 1
                    agent.add_resources(1)
                    print('Tribes: ',self.tribes['grey'].get_total_resources())
                    break

    def is_house_in_position(self, wanted_position) -> bool:
        for h in self.all_houses_list:
            if h.get_current_pos() == wanted_position:
                return True
        return False