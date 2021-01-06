from hitori_game.logic.const import PreparedMaps, Color
from hitori_game.logic.field import Field


class Map:
    def __init__(self, board, map_name):
        self.map = board
        self.map_name: PreparedMaps = map_name

    @classmethod
    def prepare_map(cls, map_name: PreparedMaps):
        board = []
        with open(map_name.value, 'r') as file:
            line = file.readline().split(' ')
            for x in range(len(line)):
                board.append([])
                for y in range(len(line)):
                    board[x].append([])
                    board[x][y] = Field(Color.GREY, int(line[y]))
            for x in range(1, len(line)):
                new_line = file.readline().split(' ')
                for y in range(len(line)):
                    board[x][y] = Field(Color.GREY, int(new_line[y]))
        return cls(board, map_name)

    def clear(self):
        self.map.clear()
