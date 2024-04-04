import pygame
import pygame_gui

class Tribe:
    def __init__(self,tribe_name : str, tribe_agents = []) -> None:
        self.__tribe_agents = tribe_agents
        self.__tribe_name = tribe_name

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

    def __repr__(self):
        return f'Tribo: {self.__tribe_name} - {self.get_tribe()}'