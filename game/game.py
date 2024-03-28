import pygame
import pygame_gui
import random

from gui.button import Button
from gui.slider import Slider

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
        #self.start_button = Button(screen=self.gui.get_screen(),x=(self.gui.get_screen_width()//3),y=(self.gui.get_screen_height()//2)-(self.gui.get_screen_height()//4),width=300,height=100,text="Start",button_color=(34, 40, 49),text_color=(238, 238, 238))
        #self.resource_slider = Slider(screen=self.gui.get_screen(),x=(self.gui.get_screen_width()//3)+25,y=(self.gui.get_screen_height()//2),height=10,length=200, min_value=0, max_value= 4000, initial_value=100)

        self.agent = Agent(self.gui.get_screen(), self.grid, current_pos=(1, 3), color=(100, 100, 100), radius=5)
        #self.resource = Resource(self.gui.get_screen(), self.grid, (random.randint(0,89), random.randint(0,89)), color=(0,128,0), radius=5)

        # Init variables for game running
        self.simulating = False
        self.game_running = True

        self.gui.draw_button()
        self.gui.draw_slider_resources()

    def run(self):
        while self.game_running:

            time_delta = self.gui.clock.tick(60) / 1000.0

            # Simulation Running Screen
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

                # Update graphic components
                self.update()
            
            # Main Menu Screen
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False

                    # Process events for the UIManager
                    self.gui.get_manager().process_events(event)

                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                            # Update slider value
                            self.gui.value_resources.set_text(f"Value: {event.value:.0f}")
                        
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.gui.start_button:
                                self.simulating = True
                                self.start_game()
                    
                    # elif event.type == pygame.MOUSEBUTTONDOWN:
                    #     mouse_pos = pygame.mouse.get_pos()
                    #     if self.start_button.is_clicked(mouse_pos):
                    #         self.start_game()
                    #         self.simulating = True
                    #self.resource_slider.handle_event(event)

                self.gui.get_screen().fill((49, 54, 63))
                self.update_start_menu()
                
            
            # Display
            self.gui.get_manager().update(time_delta)
            pygame.display.flip()

    def update(self):

        self.agent.draw()

        
        for resource in self.resources: # Desenhar todos os resources dentro da lista criada após o start
            resource.draw()

        

        self.update_pos()

    def update_start_menu(self):
        self.gui.get_manager().draw_ui(self.gui.get_screen())
        #self.gui.draw_button()
        #self.start_button.draw()
        #self.resource_slider.draw()
        #self.resource_slider.update()

    def update_pos(self):
        self.agent.rect.x, self.agent.rect.y = self.grid.check_move(self.agent.current_pos, self.agent.new_pos, self.agent)

    def start_game(self):
        '''Inicia o jogo com os recursos, tribos e tempo de regeneração dos recursos de acordo com o escolhido pelo utilizador'''
        self.resources = []
        positions = [] # Cria-se um set vazio para não termos posições repetidas
        iterations = self.gui.slider.current_value
        index = 0 # Adiciona-se um contador

        for i in range(int(iterations)):
            random_tuple = (random.randint(0,89),random.randint(0,89))
            while random_tuple in positions:
                random_tuple = (random.randint(0,89),random.randint(0,89))
            positions.append(random_tuple)
    
            self.resources.append(Resource(self.gui.get_screen(), self.grid, random_tuple, color=(0,128,0), radius=3))
            
        del positions