from enum import Enum

from v1_0.game.resources import ResourceType


class Fleet:
    def __init__(self, name, loc_system, loc_galaxy, player):
        self.fleet_id = player.next_fleet_id
        self.name = name
        self.spaceship_list = []
        self.resources = {}
        self.speed = 10  # TODO : calculate speed from the slowest spaceship
        self.loc_system = loc_system
        self.loc_galaxy = loc_galaxy
        self.player = player
        player.next_fleet_id += 1

        for t in ResourceType:
            self.resources[t.value] = 0

    def get_lower_speed(self):
        lower_speed = None
        for spaceship in self.spaceship_list:
            if lower_speed is not None and spaceship.speed > lower_speed:
                lower_speed = spaceship.speed

    def add_spaceship(self, spaceship):
        self.spaceship_list.append(spaceship)

    def get_spaceships(self):
        dic = {}

        # Inserting all types as keys
        for t in SpaceshipType:
            dic[t.value] = 0

        # Counting
        for s in self.spaceship_list:
            dic[s.spaceship_type.value] += 1
        return dic


class Spaceship:
    def __init__(self, damage, capacity, speed, spaceship_type):
        self.damage = damage
        self.capacity = capacity
        self.speed = speed
        self.spaceship_type = spaceship_type
        pass


class SpaceshipType(Enum):
    LightHunter = "Light Hunter"
    HeavyHunter = "Heavy Hunter"
    LightTransportShip = "Light Transport Ship"
    HeavyTransportShip = "Heavy transport Ship"
    Destroyer = "Destroyer"
    BattleCruiser = "Battle Cruiser"
    BattleShip = "Battle Ship"
    Colonizer = "Colonizer"


class Colonizer(Spaceship):
    def __init__(self, damage, capacity):
        super().__init__(damage, capacity, SpaceshipType.Colonizer)
        pass
