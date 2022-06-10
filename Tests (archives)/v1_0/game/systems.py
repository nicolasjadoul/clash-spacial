from v1_0.game.bases import *
from v1_0.game.constants import *


class SystemController:
    next_planet_id = 0
    next_system_id = 0
    planets_list = []
    systems_list = []

    @staticmethod
    def create_planet(name, loc, base_size):
        planet = Planet(name, loc, loc, base_size, base_size)
        SystemController.next_planet_id += 1
        SystemController.planets_list.append(planet)
        return planet

    @staticmethod
    def get_planet_from_id(pid):
        for p in SystemController.planets_list:
            if p.planet_id == pid:
                return p
        return None

    @staticmethod
    def create_system(name, location):
        system = System(name, location)
        SystemController.next_system_id += 1
        SystemController.systems_list.append(system)
        return system


class System:
    def __init__(self, name, location):
        self.id = SystemController.next_system_id
        self.name = name
        self.location = location
        self.size = {"x": SYSTEMS_DEFAULT_SIZE, "y": SYSTEMS_DEFAULT_SIZE}
        self.composition = []


class Planet:
    def __init__(self, name, loc_system, loc_galaxy, base_size_x, base_size_y):
        self.planet_id = SystemController.next_planet_id
        self.name = name
        self.base = BaseController.create_base(self, base_size_x, base_size_y)
        self.loc_system = loc_system
        self.loc_galaxy = loc_galaxy
        self.skin = "PLANET_SKIN_1"  # TODO : Implements skin system

    def __str__(self):
        return "[Planet] Name : " + str(self.name) + "\n\t" + str(self.base)


class Star:
    def __init__(self, name, location):
        self.star_id = 999,
        self.name = name,
        self.location = location
        self.skin = "STAR_SKIN_1"


class Moon(Planet):
    def __init__(self, planet, name, loc_system, loc_galaxy, base_size_x, base_size_y):
        super(Moon, self).__init__(name, loc_system, loc_galaxy, base_size_x, base_size_y)
        self.planet = planet
        pass


class Asteroid(object):
    def __init__(self, asteroid_id, name):
        self.asteroid_id = asteroid_id
        self.name = name
        pass


