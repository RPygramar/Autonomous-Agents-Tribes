class Tribe:
    def __init__(self, color: tuple, tribe_name: str) -> None:
        self.__tribe_agents = []
        self.__houses = []
        self.__tribe_name = tribe_name
        self.__color = color
        self.__confidence = 0

    def get_tribe(self) -> list:
        return self.__tribe_agents
    
    def get_color(self) -> tuple:
        return self.__color
    
    def set_confidence(self, confidence):
        self.__confidence = confidence
        print(self.__tribe_name,self.__confidence)
        for agent in self.get_tribe():
            agent.set_confidence(confidence)

    def get_confidence(self) -> float:
        return self.__confidence
    
    def get_confidence_levels(self) -> float:
        total_confidence = 0
        for agent in self.get_tribe():
            total_confidence += agent.get_confidence()
        if self.get_tribe():
            return (total_confidence / len(self.get_tribe()))
        return total_confidence

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
        for house in self.get_houses():
            total_resources += house.get_storage()
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
            if agent is None:
                break
            agent.run_agent(resource_list)
    
    def check_enemy_in_territory(self, enemies):
        for house in self.get_houses():    
            house.call_help(enemies=[enemy for enemy in enemies if enemy.rect.colliderect(house.territory_area)],
                            agents=[agent for agent in self.get_tribe() if house.territory_area.colliderect(agent.rect)])
                        
    def reproduce_agents(self):
        for house in self.get_houses():
            if house.get_storage() == house.get_storage_limit():
                house.set_storage(0)
                return house

    def heal_agent(self, agent):
        if agent.check_need_heal():
            for house in self.get_houses():
                if house.territory_area.colliderect(agent.rect) and house.get_storage() != 0:
                    agent.move_Astar([house])
                    house.heal_agent(agent)
                    break

    def run_tribe(self, resource_list=[],enemy_agents_list=[]) -> None:
        for house in self.__houses:
            if house.health <= 0:
                self.__houses.remove(house)
            else:
                enemy_in_house_territory = [enemy for enemy in enemy_agents_list if enemy.rect.colliderect(house.territory_area)]
                self.check_enemy_in_territory(enemy_in_house_territory)
                for enemy_agent in enemy_in_house_territory:
                    if enemy_agent.attack_area.colliderect(house.territory_area):
                        house.take_damage(enemy_agent.attack_power)

        for agent in self.__tribe_agents:
            if agent.health <= 0:
                agent.clear_path()
                self.__tribe_agents.remove(agent)
                return agent
            else:
                self.heal_agent(agent)
                agent.run_agent(resources=resource_list, houses=self.get_houses(), team_agents=self.get_tribe())
                for enemy_agent in enemy_agents_list:
                    if agent.attack_area.colliderect(enemy_agent.rect):
                        enemy_agent.take_damage(agent.attack_power)
                agent.draw()
        self.check_enemy_in_territory(enemy_agents_list)

    def __repr__(self):
        return f'Tribo: {self.__tribe_name} - \n {self.get_tribe()} \n {self.get_houses()}'