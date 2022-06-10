from enum import Enum

import prod
from prod.game.game import *
from prod.game.resources import ResourceType
from prod.game.utils import Location
from prod.game.constants import *


class Fleet:
    def __init__(self, name, loc_system, loc_galaxy, player):
        self.fleet_id = player.next_fleet_id
        self.name = name
        self.spaceship_list = []
        self.destination = None
        self.resources = {}
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
            elif lower_speed is None:
                lower_speed = spaceship.speed
        return lower_speed

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

    def move_to_destination(self):
        travellable = self.get_lower_speed()

        while travellable > 0:
            to_travel_x = abs(self.loc_system.point.x - self.destination.point.x)
            to_travel_y = abs(self.loc_system.point.y - self.destination.point.y)
            if to_travel_x > to_travel_y:
                # More distance on x, we travel on x
                if self.destination.point.x > self.loc_system.point.x:
                    # We're on the right, move to left
                    self.player.move_fleet(self, Location(self.loc_system.point.x + 1, self.loc_system.point.y))
                elif self.destination.point.x < self.loc_system.point.x:
                    # We're on the left, move to right
                    self.player.move_fleet(self, Location(self.loc_system.point.x - 1, self.loc_system.point.y))
            else:
                # More distance on y, we travel on y
                if self.destination.point.y > self.loc_system.point.y:
                    # We're on the bottom, move to top
                    self.player.move_fleet(self, Location(self.loc_system.point.x, self.loc_system.point.y + 1))
                elif self.destination.point.y < self.loc_system.point.y:
                    # We're on the top, move to bottom
                    self.player.move_fleet(self, Location(self.loc_system.point.x, self.loc_system.point.y - 1))
            travellable -= 1

        if self.destination.point.x == self.loc_system.point.x and self.destination.point.y == self.loc_system.point.y:
            self.destination = None

    def attack(self, enemy_fleet):
        print("Fleet ", self.fleet_id, " attacks fleet ", enemy_fleet.fleet_id)
        self_attack, self_defense = self.get_fight_stats()
        enemy_attack, enemy_defense = enemy_fleet.get_fight_stats()

        enemy_hp = enemy_defense - self_attack
        self_hp = self_defense - enemy_attack

        if enemy_hp < 0:
            enemy_fleet.explode()
        else:
            hp_lost = self_attack/len(enemy_fleet.spaceship_list)
            for s in enemy_fleet.spaceship_list:
                s.hp -= hp_lost

        if self_hp < 0:
            self.explode()
        else:
            hp_lost = enemy_attack / len(self.spaceship_list)
            for s in self.spaceship_list:
                s.hp -= hp_lost

    def explode(self):
        print("Fleet ", self.fleet_id, " exploded")
        self.player.fleet_list.remove(self)
        prod.game.game.Game.system.composition.remove(self)

    def get_fight_stats(self):
        attack, defense = 0, 0
        for s in self.spaceship_list:
            attack += s.damage
            defense += s.hp
        return attack, defense


class Spaceship:
    def __init__(self, spaceship_type):
        hp, damage, capacity, speed = 0, 0, 0, 0
        if spaceship_type == SpaceshipType.LightHunter:
            hp, damage, capacity, speed = LIGHTHUNTER_HP, LIGHTHUNTER_DAMAGE, LIGHTHUNTER_CAPACITY, LIGHTHUNTER_SPEED
        elif spaceship_type == SpaceshipType.HeavyHunter:
            hp, damage, capacity, speed = HEAVYHUNTER_HP, HEAVYHUNTER_DAMAGE, HEAVYHUNTER_CAPACITY, HEAVYHUNTER_SPEED
        elif spaceship_type == SpaceshipType.LightTransportShip:
            hp, damage, capacity, speed = LTS_HP, LTS_DAMAGE, LTS_CAPACITY, LTS_SPEED
        elif spaceship_type == SpaceshipType.HeavyTransportShip:
            hp, damage, capacity, speed = HTS_HP, HTS_DAMAGE, HTS_CAPACITY, HTS_SPEED
        elif spaceship_type == SpaceshipType.Destroyer:
            hp, damage, capacity, speed = DESTROYER_HP, DESTROYER_DAMAGE, DESTROYER_CAPACITY, DESTROYER_SPEED
        elif spaceship_type == SpaceshipType.BattleCruiser:
            hp, damage, capacity, speed = BATTLECRUISER_HP, BATTLECRUISER_DAMAGE, BATTLECRUISER_CAPACITY, BATTLECRUISER_SPEED
        elif spaceship_type == SpaceshipType.BattleShip:
            hp, damage, capacity, speed = BATTLESHIP_HP, BATTLESHIP_DAMAGE, BATTLESHIP_CAPACITY, BATTLESHIP_SPEED
        elif spaceship_type == SpaceshipType.Colonizer:
            hp, damage, capacity, speed = COLONIZER_HP, COLONIZER_DAMAGE, COLONIZER_CAPACITY, COLONIZER_SPEED

        self.hp = hp
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
    def __init__(self):
        super().__init__(self)
        pass
