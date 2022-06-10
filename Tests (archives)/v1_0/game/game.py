from v1_0.game.spaceships import *
from v1_0.game.systems import *
from v1_0.game.bases import *
from v1_0.game.player import *
from v1_0.game.utils import Location


class Game:
    turn = 0
    players = []
    systems = []

    @staticmethod
    def next_turn():
        Game.turn += 1
        print("===> Next turn")

    @staticmethod
    def start():
        print("===> Game starts")
        UniverseGenerator.gen()
        sols = Game.systems[0]
        """ BASE TESTING """

        """ PLAYER TESTING """
        p = PlayerController.create_player("Armand")
        Game.players.append(p)
        p.gold = 168554
        p.create_spaceship(Location(), 400, 300, 2, SpaceshipType.Colonizer)
        p.create_spaceship(Location(1, 1), 400, 300, 2, SpaceshipType.Colonizer)
        p.move_fleet(p.fleet_list[0], Location(1, 1))
        p.planets_list.append(sols.composition[5])
        sols.composition.append(p.fleet_list[0])

        p.fleet_list.append(Fleet("Flotte beta", Location(1, 2), Location(1, 2), p))

        a = Alliance("Star Patrol")
        a.add_player(p)
        """ JSON TESTING """
        # print(JsonBuilder.build_fleet(p.fleet_list[0]))
        # print(JsonBuilder.build_building(jupiter.base.buildings_list[0]))
        # print(JsonBuilder.build_base(jupiter.base)[1])
        # print(JsonBuilder.build_planet(jupiter)[1])
        # JsonSaver.create_json_file(JsonBuilder.build_player(p)[0], 'data/examples/Player.json')
        # JsonSaver.create_json_file(JsonBuilder.build_planet(jupiter)[0], 'data/examples/Planet.json')
        # JsonSaver.create_json_file(JsonBuilder.build_system(sols)[0], 'data/examples/System.json')


class UniverseGenerator:
    @staticmethod
    def gen():  # TODO : Improvement - procedural generation
        sun = Star("Sun", Location(13, 13))
        mercury = SystemController.create_planet("Mercure", Location(14, 15), SMALL_BASE_SIZE)
        venus = SystemController.create_planet("Venus", Location(11, 17), MEDIUM_BASE_SIZE)
        earth = SystemController.create_planet("Terre", Location(10, 11), MEDIUM_BASE_SIZE)
        mars = SystemController.create_planet("Mars", Location(15, 9), SMALL_BASE_SIZE)
        jupiter = SystemController.create_planet("Jupiter", Location(19, 11), BIG_BASE_SIZE)
        saturn = SystemController.create_planet("Saturne", Location(18, 21), BIG_BASE_SIZE)
        uranus = SystemController.create_planet("Uranus", Location(6, 9), BIG_BASE_SIZE)
        neptune = SystemController.create_planet("Neptune", Location(13, 3), BIG_BASE_SIZE)
        pluto = SystemController.create_planet("Pluton", Location(5, 23), SMALL_BASE_SIZE)

        for bt in BuildingType:
            BaseController.create_building(jupiter.base, bt, Location(random.randint(0, 10), random.randint(0, 10)))

        sols = SystemController.create_system("Système solaire", Location(10, 10))
        sols.composition.extend([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto])

        Game.systems.append(sols)
        print("===> Systems generated")
