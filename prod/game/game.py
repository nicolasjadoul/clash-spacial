from prod.game.spaceships import *
from prod.game.systems import *
from prod.game.bases import *
from prod.game.player import *
from prod.game.systems import Planet
from prod.game.utils import Location


class Game:
    turn = 0
    players = []
    system = None

    @staticmethod
    def next_turn():
        Game.turn += 1
        print("\n=========================")
        print("===> TURN ", Game.turn, " IS STARTING")
        print("=========================")

        for c in Game.system.composition:
            # Fleets movement
            if isinstance(c, Fleet) and c.destination is not None:
                c.move_to_destination()
            elif isinstance(c, Fleet) and len(Game.system.get_fleets_at_pos(c.loc_system)) > 1:
                list_without_himself = Game.system.get_fleets_at_pos(c.loc_system).copy()
                list_without_himself.remove(c)
                if list_without_himself[0].player != c.player:
                    c.attack(list_without_himself[0])
            # Bases production
            elif isinstance(c, Planet):
                c.base.next_turn_production()


    @staticmethod
    def start():
        print("===> Game starts")
        UniverseGenerator.gen()
        """ BASE TESTING """

        """ PLAYER TESTING """
        p = PlayerController.create_player("Armand")
        p2 = PlayerController.create_player("Elie")
        Game.players.append(p)
        Game.players.append(p2)
        p.gold = 168554
        p.create_spaceship(Location(), SpaceshipType.Destroyer)
        p.create_spaceship(Location(), SpaceshipType.Destroyer)
        p.create_spaceship(Location(), SpaceshipType.Destroyer)
        p2.create_spaceship(Location(), SpaceshipType.Destroyer)
        p.planets_list.append(Game.system.composition[5])
        Game.system.composition.append(p.fleet_list[0])
        Game.system.composition.append(p2.fleet_list[0])

        p.fleet_list.append(Fleet("Flotte beta", Location(1, 2), Location(1, 2), p))

        # p.fleet_list[0].destination = Location(5, 10)

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
            if bt != BuildingType.Mine:
                BaseController.create_building(jupiter.base, bt, Location(random.randint(0, 10), random.randint(0, 10)),
                                               [])
            else:
                BaseController.create_building(jupiter.base, bt, Location(random.randint(0, 10), random.randint(0, 10)),
                                               ResourceType.Steel)
                BaseController.create_building(jupiter.base, bt, Location(random.randint(0, 10), random.randint(0, 10)),
                                               ResourceType.Crystal)
                BaseController.create_building(jupiter.base, bt, Location(random.randint(0, 10), random.randint(0, 10)),
                                               ResourceType.Uranium)

        sols = SystemController.create_system("Système solaire", Location(10, 10))
        sols.composition.extend([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto])

        Game.system = sols
        print("===> Systems generated")
