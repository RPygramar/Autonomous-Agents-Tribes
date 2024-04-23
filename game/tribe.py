from threading import Event, Thread
import time
import pygame
import pygame_gui
import asyncio
from multiprocessing import Process
import queue

class Tribe:
    def __init__(self,tribe_name : str, tribe_agents : list = [], tribe_houses : list = []) -> None:
        self.__tribe_agents = tribe_agents
        self.__houses = tribe_houses
        self.__tribe_name = tribe_name
        self.tribe_thread = None
        # self.tribe_running = Event()
        self.q = queue.Queue()

    def get_tribe(self) -> list:
        return self.__tribe_agents
    
    def add_agent(self, agent : object) -> None:
        self.__tribe_agents.append(agent)

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

    def start_tribe(self, resources_list):
        """Start the background management of tribe agents."""
        if self.tribe_thread is None or not self.tribe_thread.is_alive():
            self.tribe_running.set()  # Signal that the tribe should be running
            self.tribe_thread = Thread(target=self.run_tribe, args=(resources_list,))
            self.tribe_thread.start()

    def stop_tribe(self):
        """Stop the background management of tribe agents."""
        self.tribe_running.clear()  # Signal to stop the loop

    # def run_tribe(self, resources_list):
    #     """Run in a background thread to manage agents."""
    #     print('STARTED TRIBE RUNNING')
    #     while self.tribe_running.is_set():
    #         for agent in self.__tribe_agents:
    #             if not self.tribe_running.is_set():
    #                 break  # Exit if no longer running
    #             agent.run_agent(resources_list)
    #             agent.draw()
    #         #time.sleep(0.1)  # Prevent this loop from hogging CPU, adjust as needed
    #     print('ENDED TRIBE RUNNING')

    def __worker(self,resource_list):
        while True:
            agent = self.q.get()
            if agent is None:
                break
            agent.run_agent(resource_list)
            agent.draw()
            print(f'Running Agent {agent} finished')
            self.q.task_done()

    def run_tribe(self, resources_list) -> None:
        Thread(target=self.__worker, args=(resources_list, ), daemon=True).start()
        for agent in self.__tribe_agents:
            self.q.put(agent)
        
        # self.q.join()
        # self.q.put(None)
        
        print('All agents completed')


    def __repr__(self):
        return f'Tribo: {self.__tribe_name} - \n {self.get_tribe()} \n {self.get_houses()}'