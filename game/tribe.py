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

    # def start_tribe(self, resources_list):
    #     """Start the background management of tribe agents."""
    #     if self.tribe_thread is None or not self.tribe_thread.is_alive():
    #         self.tribe_running.set()  # Signal that the tribe should be running
    #         self.tribe_thread = Thread(target=self.run_tribe, args=(resources_list,))
    #         self.tribe_thread.start()

    # def stop_tribe(self):
    #     """Stop the background management of tribe agents."""
    #     self.tribe_running.clear()  # Signal to stop the loop

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
    
    def run_tribe(self, resource_list=[],agents_list=[]) -> None:
        for agent in self.__tribe_agents:
            if agent.health <= 0:
                agent.clear_path()
                self.__tribe_agents.remove(agent)
                print(self.get_tribe_name(), 'died')
                return agent
            else:
                agent.run_agent(resource_list)
                for enemy_agent in agents_list:
                    if agent.attack_area.colliderect(enemy_agent.rect):
                        enemy_agent.take_damage(agent.attack_power)
                        print(self.get_tribe_name(),agent.health)
                agent.draw()
        
                


        
        # self.q.join()
        # self.q.put(None)
    
    # def run_tribe(self, resources_list) -> None:
    #     for agent in self.__tribe_agents:
    #         agent.run_agent(resources_list)
    #         agent.draw()


    def __repr__(self):
        return f'Tribo: {self.__tribe_name} - \n {self.get_tribe()} \n {self.get_houses()}'