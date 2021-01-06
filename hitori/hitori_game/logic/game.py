from hitori_game.logic.const import PreparedMaps
from hitori_game.logic.map import Map
from hitori_game.logic.solver import Solver


class Game:
    def __init__(self):
        self.map = None
        self.solver = None

    def prepare_game(self, map_name: PreparedMaps):
        self.map = Map.prepare_map(map_name)
        self.solver = Solver()

    def change_field_color(self, field_pos: tuple):
        self.map.map[field_pos[0]][field_pos[1]].change_color()

    def solve(self):
        self.map.map = self.solver.solve_puzzle(
            Map.prepare_map(self.map.map_name).map)

    def check_player(self):
        bot_map = self.solver.solve_puzzle(
            Map.prepare_map(self.map.map_name).map)
        for x in range(len(bot_map)):
            for y in range(len(bot_map)):
                if not self.map.map[x][y].color == bot_map[x][y].color:
                    self.map.map[x][y].set_red()

    def reset(self):
        self.map.clear()
