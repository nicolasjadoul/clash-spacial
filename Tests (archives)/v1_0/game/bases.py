import random
from enum import Enum

from v1_0.game.resources import ResourceType
from v1_0.game.spaceships import SpaceshipType
from v1_0.game.systems import *

"""
    BASES
"""


class BaseController:
    instance = None
    next_base_id = 0
    next_building_id = 0

    def __init__(self):
        pass

    @staticmethod
    def create_base(planet, size_x, size_y):
        base = Base(planet, size_x, size_y)
        BaseController.next_base_id += 1
        return base

    @staticmethod
    def create_building(parent_base, building_type, location):
        new_building = None
        if building_type == BuildingType.DefensiveTurret:
            new_building = DefensiveTurret(location)
        elif building_type == BuildingType.Garage:
            new_building = Garage(location)
        elif building_type == BuildingType.Habitation:
            new_building = Habitation(location)
        elif building_type == BuildingType.Mine:
            new_building = Mine(location)
        elif building_type == BuildingType.NuclearPlant:
            new_building = NuclearPlant(location)
        elif building_type == BuildingType.ResearchCenter:
            new_building = ResearchCenter(location)
        elif building_type == BuildingType.SolarPanel:
            new_building = SolarPanel(location)
        elif building_type == BuildingType.Warehouse:
            new_building = Warehouse(location)

        BaseController.next_building_id += 1
        parent_base.buildings_list.append(new_building)


class Base:
    def __init__(self, planet, size_x, size_y):
        self.base_id = BaseController.next_base_id
        self.buildings_list = []
        self.planet = planet
        self.size = {"x": size_x, "y": size_y}
        self.resources = {}
        self.storage = {ResourceType.Steel.value: 1000,
                        ResourceType.Uranium.value: 500,
                        ResourceType.Crystal.value: 100}
        self.production = {ResourceType.Steel.value: 50,
                           ResourceType.Uranium.value: 25,
                           ResourceType.Crystal.value: 5}
        self.spaceships = {}
        for t in SpaceshipType:
            self.spaceships[t.value] = random.randint(0, 100)

        for t in ResourceType:
            self.resources[t.value] = 0

        self.resources[ResourceType.Population.value] = {"total": 0, "used": 0}

    def get_id(self):
        return self.base_id

    def get_buildings_list(self):
        return self.buildings_list

    def __str__(self):
        buildings_str = ""
        for b in self.buildings_list:
            buildings_str += "\t• " + str(b) + "\n"
        if len(buildings_str) == 0:
            buildings_str = "\t• No building"
        return "[Base] ID : " + str(self.base_id) + "\n" + buildings_str


"""
    BUILDINGS
"""


class BuildingType(Enum):
    DefensiveTurret = "Defensive Turret"
    Garage = "Garage"
    Habitation = "Habitation"
    Mine = "Mine"
    NuclearPlant = "Nuclear Plant"
    ResearchCenter = "Research Center"
    SolarPanel = "Solar Panel"
    Warehouse = "Warehouse"


class Building:
    def __init__(self, name, location):
        self.building_id = BaseController.next_building_id
        self.name = name
        self.location = location
        self.level = 1
        pass

    def __str__(self):
        return "[Building] ID : " + str(self.building_id) + " - Name : " + self.name + " - Level : " + str(self.level) \
               + " - Location : [" + str(self.location.point.x) + ", " + str(self.location.point.y) + "]"


class DefensiveTurret(Building):
    def __init__(self, location):
        super(DefensiveTurret, self).__init__(BuildingType.DefensiveTurret.value, location)
        pass


class Garage(Building):
    def __init__(self, location):
        super(Garage, self).__init__(BuildingType.Garage.value, location)
        pass


class Habitation(Building):
    def __init__(self, location):
        super(Habitation, self).__init__(BuildingType.Habitation.value, location)
        pass


class Mine(Building):
    def __init__(self, location):
        super(Mine, self).__init__(BuildingType.Mine.value, location)
        pass


class NuclearPlant(Building):
    def __init__(self, location):
        super(NuclearPlant, self).__init__(BuildingType.NuclearPlant.value, location)
        pass


class ResearchCenter(Building):
    def __init__(self, location):
        super(ResearchCenter, self).__init__(BuildingType.ResearchCenter.value, location)
        pass


class SolarPanel(Building):
    def __init__(self, location):
        super(SolarPanel, self).__init__(BuildingType.SolarPanel.value, location)
        pass


class Warehouse(Building):
    def __init__(self, location):
        super(Warehouse, self).__init__(BuildingType.Warehouse.value, location)
        pass
