from enum import Enum


class Resource(object):
    def __init__(self, name):
        self.name = name
        pass


class ResourceType(Enum):
    Steel = "Steel"
    Crystal = "Crystal"
    Uranium = "Uranium"
    Gold = "Gold"
    Energy = "Energy"
    Population = "Population"
