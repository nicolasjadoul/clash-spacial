from prod.game.game import Game
from prod.game.json_utils import JsonBuilder
from prod.game.player import PlayerController
from prod.game.systems import SystemController


class ClientInterface:
    @staticmethod
    def get_player(pid):
        player = PlayerController.get_player_from_id(int(pid))
        if player is None:
            return {"error": "No player with ID " + pid}
        else:
            return JsonBuilder.build_player(player)[0]

    @staticmethod
    def get_planet(pid):
        planet = SystemController.get_planet_from_id(int(pid))
        if planet is None:
            return {"error": "No planet with ID " + pid}
        else:
            return JsonBuilder.build_planet(planet)[0]

    @staticmethod
    def get_system():
        if Game.system is None:
            return {"error": "No system found"}
        else:
            return JsonBuilder.build_system(Game.system)[0]
