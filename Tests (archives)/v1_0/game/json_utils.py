import json
from v1_0.game.constants import *
import os

from v1_0.game.systems import Planet, Star, Moon


class DicBuilder:
    @staticmethod
    def build_planet(planet):
        dic = {
            "type": "planet",
            "id": planet.planet_id,
            "name": planet.name,
            "skin": planet.skin,
            "positions": {
                "posGalaxy": {"x": planet.loc_galaxy.point.x, "y": planet.loc_galaxy.point.y},
                "posSystem": {"x": planet.loc_system.point.x, "y": planet.loc_system.point.y}
            },
            "base": DicBuilder.build_base(planet.base)
        }
        return dic

    @staticmethod
    def build_star(star):
        dic = {
            "type": "star",
            "id": star.star_id,
            "name": star.name,
            "skin": star.skin,
            "position": {"x": star.location.point.x, "y": star.location.point.y}
        }
        return dic

    @staticmethod
    def build_base(base):
        dic = {
            "id": base.base_id,
            "size": {"x": base.size["x"], "y": base.size["y"]}
        }
        return dic

    @staticmethod
    def build_fleet(fleet):
        dic = {"id": fleet.fleet_id,
               "name": fleet.name,
               "speed": fleet.speed,
               "positions": {
                   "posGalaxy": {"x": fleet.loc_galaxy.point.x, "y": fleet.loc_galaxy.point.y},
                   "posSystem": {"x": fleet.loc_system.point.x, "y": fleet.loc_system.point.y}
               },
               "spaceships": fleet.get_spaceships(),
               "resources": fleet.resources
               }
        return dic


class JsonBuilder:
    @staticmethod
    def build_player(player):
        # Alliance dictionary
        dic_alliance = None
        if player.alliance is not None:
            dic_alliance = {"id": player.alliance.id, "name": player.alliance.name}

        # Fleets list
        list_fleets = []
        for f in player.fleet_list:
            list_fleets.append(DicBuilder.build_fleet(f))

        # Possessions list
        list_possessions = []
        for p in player.planets_list:
            list_possessions.append(DicBuilder.build_planet(p))

        # Player dictionary
        player_dic = {
            "active": player.active,
            "alliance": dic_alliance,
            "fleets": list_fleets,
            "gold": player.gold,
            "id": player.player_id,
            "mail": "adresse@email.fr",  # TODO : get @ from database through player's ID
            "name": player.name,
            "possessions": list_possessions
        }

        return player_dic, json.dumps(player_dic, indent=JSON_INDENT)

    @staticmethod
    def build_building(building):
        dic = {
            "id": building.building_id,
            "name": building.name,
            "x": building.location.point.x,
            "y": building.location.point.y,
            "level": building.level
        }
        return dic, json.dumps(dic, indent=JSON_INDENT)

    @staticmethod
    def build_game(game):
        dic = {
            "turn": game.turn,
            "players": {},
            "systems": {}
        }
        for p in game.players:
            dic["players"][p.name] = JsonBuilder.build_player(p)[0]

        return dic, json.dumps(dic, indent=JSON_INDENT)

    @staticmethod
    def build_planet(planet):
        base_tile_map = []
        for b in planet.base.buildings_list:
            base_tile_map.append({"x": b.location.point.x,
                                  "y": b.location.point.y,
                                  "building": b.name,
                                  "level": b.level
                                  })

        planet_dic = {
            "type": "planet",
            "id": planet.planet_id,
            "name": planet.name,
            "skin": planet.skin,
            "size": {"x": planet.base.size["x"], "y": planet.base.size["y"]},
            "resources": planet.base.resources,
            "storage": planet.base.storage,
            "production": planet.base.production,
            "spaceships": planet.base.spaceships,
            "baseTileMap": base_tile_map
        }
        return planet_dic, json.dumps(planet_dic, indent=JSON_INDENT)

    @staticmethod
    def build_system(system):
        composition_list = []

        for c in system.composition:
            component = {}
            if isinstance(c, Planet):
                component = DicBuilder.build_planet(c)
            elif isinstance(c, Star):
                component = DicBuilder.build_star(c)
            elif isinstance(c, Moon):
                component = DicBuilder.build_planet(c)
            else:
                component = DicBuilder.build_fleet(c)
                component["type"] = "fleet"
            composition_list.append(component)

        system_dic = {
            "id": system.id,
            "name": system.name,
            "position": {"x": system.location.point.x, "y": system.location.point.y},
            "size":  {"x": system.size["x"], "y": system.size["y"]},
            "composition": composition_list
        }

        return system_dic, json.dumps(system_dic, indent=JSON_INDENT)


class JsonSaver:
    @staticmethod
    def create_json_file(data, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as out:
            json.dump(data, out, indent=JSON_INDENT)
