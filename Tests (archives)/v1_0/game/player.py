from v1_0.game.spaceships import *
from v1_0.game.utils import *


class PlayerController:
    instance = None
    next_player_id = 0
    players_list = []

    def __init__(self):
        pass

    @staticmethod
    def create_player(name):
        player = Player(name)
        PlayerController.players_list.append(player)
        PlayerController.next_player_id += 1
        return player

    @staticmethod
    def add_alliance(alliance, player):
        player.alliance = alliance
        alliance.members.append(player)

    @staticmethod
    def get_instance():
        if PlayerController.instance is None:
            PlayerController.instance = PlayerController()

        return PlayerController.instance

    @staticmethod
    def get_player_from_id(pid):
        for p in PlayerController.players_list:
            if p.player_id == pid:
                return p
        return None


class Player:
    next_fleet_id = 0

    def __init__(self, name):
        self.player_id = PlayerController.next_player_id
        self.active = False
        self.name = name
        self.fleet_list = []
        self.planets_list = []
        self.alliance = None
        self.gold = 0

    def create_spaceship(self, location, damage, capacity, speed, spaceship_type):
        spaceship = Spaceship(damage, capacity, speed, spaceship_type)
        fleet = self.test_fleet(location)
        if fleet is not None:
            fleet.add_spaceship(spaceship)
        else:
            fleet = Fleet("Flotte", location, location, self)  # TODO : 2nd location must be galaxy one
            fleet.add_spaceship(spaceship)
            self.fleet_list.append(fleet)

    def move_fleet(self, fleet, location):
        n_fleet = self.test_fleet(location)
        if n_fleet is not None:
            for spaceship in fleet.spaceship_list:
                n_fleet.add_spaceship(spaceship)
            self.fleet_list.remove(fleet)
        else:
            fleet.location = location

    def test_fleet(self, location):
        for fleet in self.fleet_list:
            if location.equals(fleet.loc_system):
                return fleet
        return None
    #def battle(self, fleet1, fleet2):


class Alliance:
    next_alliance_id = 0

    def __init__(self, name):
        self.members = []
        self.id = Alliance.next_alliance_id
        self.name = name
        Alliance.next_alliance_id += 1
        pass

    def add_player(self, player):
        self.members.append(player)
        player.alliance = self


