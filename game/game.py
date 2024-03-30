import pygame
import pygame_gui
import random

from agents.agent import Agent
from resources.resource_algorithm import Resource
from game.grid import Grid
from gui.gui import GUI


class Game:
    def __init__(self):

        # Init interface
        self.gui = GUI()
        self.grid = Grid(self.gui)
        self.grid.load_map()


        # Init main menu
        self.gui.draw_button()
        self.gui.draw_slider_resources()


        # TEST AGENT
        self.agent = Agent(self.gui.get_screen(), self.grid, current_pos=(1, 3), color=(100, 100, 100), radius=5)


        # Init variables for game running
        self.simulating = False
        self.game_running = True

        
    # MÉTODO QUE MANIPULA O JOGO
    def run(self):
        while self.game_running:

            time_delta = self.gui.clock.tick(60) / 1000.0

            # Screen da Simulação
            if self.simulating:                   
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            self.agent.move_up()
                        elif event.key == pygame.K_s:
                            self.agent.move_down()
                        elif event.key == pygame.K_d:
                            self.agent.move_right()
                        elif event.key == pygame.K_a:
                            self.agent.move_left()
                # Fill background color
                self.gui.get_screen().fill(self.gui.bg_color)    

                # Update aos componentes da simulação
                self.update()
            
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
                                self.simulating = True
                                self.start_game()

                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                
            
            # Display
            self.gui.get_manager().update(time_delta)
            pygame.display.flip()

    def update(self):
        '''Desenha os diferentes objetos para a simulação'''
        
        for resource in self.resources: # Desenhar todos os resources dentro da lista criada após o start
            resource.draw()

        self.agent.draw()

        self.update_pos()

        self.check_collisions()

    def update_start_menu(self):
        '''Desenha os elementos do Menu Inicial'''
        self.gui.get_manager().draw_ui(self.gui.get_screen())

    def update_pos(self):
        self.agent.rect.x, self.agent.rect.y = self.grid.check_move(self.agent.current_pos, self.agent.new_pos, self.agent)

    def start_game(self):
        '''Inicia o jogo com os recursos, tribos e tempo de regeneração dos recursos de acordo com o escolhido pelo utilizador'''
        self.resources = []
        positions = [] # Cria-se uma lista vazia para preencher todas as posições com recursos
        iterations = self.gui.slider.current_value

        for i in range(int(iterations)): # Popula-se a lista positions com posições aleatórias e distintas
            random_tuple = (random.randint(0,89),random.randint(0,89))
            while random_tuple in positions:
                random_tuple = (random.randint(0,89),random.randint(0,89))
            positions.append(random_tuple)
    
            self.resources.append(Resource(self.gui.get_screen(), self.grid, random_tuple, color=(0,128,0), radius=3)) # Popula-se a lista resources com as shapes "resource"
            
        del positions # elimina-se a lista para não ocupar memória

    def check_collisions(self):
        for resourse in self.resources:
            if self.agent.rect.colliderect(resourse.rect):
                resourse.set_drawing(False)