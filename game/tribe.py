from threading import Event, Thread
import time
import pygame
import pygame_gui
import asyncio
from multiprocessing import Process
import queue

class Tribe:
    # def __init__(self, color : tuple, tribe_name : str, tribe_agents : list = [], tribe_houses : list = []) -> None:
    #     self.__tribe_agents = tribe_agents
    #     self.__houses = tribe_houses
    #     self.__tribe_name = tribe_name
    #     self.__color = color
    def __init__(self, color: tuple, tribe_name: str) -> None:
        self.__tribe_agents = []
        self.__houses = []
        self.__tribe_name = tribe_name
        self.__color = color
        # self.tribe_thread = None
        # self.tribe_running = Event()
        # self.q = queue.Queue()

    def get_tribe(self) -> list:
        return self.__tribe_agents
    
    def get_color(self) -> tuple:
        return self.__color
    
    def add_agent(self, agent : object) -> None:
        # print(agent)
        self.__tribe_agents.append(agent)
        # print(self.__tribe_agents)

    def remove_agent(self, agent : object) -> None:
        for a in self.__tribe_agents:
            if agent == a:
                self.__tribe_agents.remove(agent)
                break

    def get_total_resources(self) -> int:
        total_resources = 0
        for agent in self.get_tribe():
            total_resources += agent.get_resources()
        return total_resources

    def get_tribe_name(self) -> str:
        return self.__tribe_name
    
    def set_tribe_name(self, name: str) -> None:
        self.__tribe_name = name

    def get_houses(self) -> list:
        return self.__houses

    def add_house(self, house: object) -> None:
        self.__houses.append(house)

    def __worker(self,resource_list):
        while True:
            agent = self.q.get()
            #print(f"[TRIBE] Agent {agent} created!")
            if agent is None:
                break
            agent.run_agent(resource_list)
            #agent.draw()
            #print("Queue size:", self.q.qsize())
            # self.q.task_done()

    # def run_tribe(self, resources_list) -> None:
    #     t = Thread(target=self.__worker, args=(resources_list, ), daemon=True)
    #     #print(f"[TRIBE] Tribe {self.get_tribe_name()} created!")
    #     t.start()
    #     for agent in self.__tribe_agents:
    #         self.q.put(agent)
    
    def reproduce_agents(self):
        for house in self.get_houses():
            if house.get_storage() == house.get_storage_limit():
                house.set_storage(0)
                return house
                

                    # a casa está a manter os recursos!!!
                        
    def run_tribe(self, resource_list=[],agents_list=[]) -> None:
        for house in self.__houses:
            if house.health <= 0:
                self.__houses.remove(house)
            else:
                for enemy_agent in agents_list:
                    if enemy_agent.attack_area.colliderect(house.territory_area):
                        house.take_damage(enemy_agent.attack_power)

        for agent in self.__tribe_agents:
            if agent.health <= 0:
                agent.clear_path()
                self.__tribe_agents.remove(agent)
                #print(self.get_tribe_name(), 'died')
                return agent
            else:
                agent.run_agent(resources=resource_list,houses=self.get_houses())
                for enemy_agent in agents_list:
                    if agent.attack_area.colliderect(enemy_agent.rect):
                        enemy_agent.take_damage(agent.attack_power)
                agent.draw()
            #if len(self.get_tribe()) >= 2:
             #   print(self.get_tribe()[1], self.get_tribe()[1].get_resources(), self.get_tribe()[1].colliding_with_house_territory(self.get_houses()))
                        # print(len(self.get_tribe()))
                        # print(agent, agent.get_resources())
        #print(self.get_houses())
        
                


        
        # self.q.join()
        # self.q.put(None)
    
    # def run_tribe(self, resources_list) -> None:
    #     for agent in self.__tribe_agents:
    #         agent.run_agent(resources_list)
    #         agent.draw()


    def __repr__(self):
        return f'Tribo: {self.__tribe_name} - \n {self.get_tribe()} \n {self.get_houses()}'