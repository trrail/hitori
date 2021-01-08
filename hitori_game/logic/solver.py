from hitori_game.logic.const import Color, DIRECTIONS


class Solver:
    def solve_puzzle(self, map: list) -> list:
        for i in range(10):
            for x in range(len(map)):
                for y in range(len(map)):
                    self.check_three_in_row((x, y), map)
                    self.get_color_in_pos((x, y), map)
                    self.check_quad_middle((x, y), map)
                    if map[x][y].color == Color.GREY:
                        self.check_pair_isolation((x, y), map)
        return map

    def get_color_in_pos(self, field_pos: tuple, map: list):
        for part in range(len(map)):
            if part != field_pos[0]:
                self.check_row(field_pos, pos=(part, field_pos[1]), map=map)
            if part != field_pos[1]:
                self.check_row(field_pos, (field_pos[0], part), map)
        if not map[field_pos[0]][field_pos[1]].have_near_another_field:
            map[field_pos[0]][field_pos[1]].set_white()

    '''
    field_pos - координаты изначальной точки
    pos - координаты точки, лежащей либо на одной вертикали, либо на одной
    горизонтали, что и изначальная точка
    map - карта игры
    '''
    def check_row(self, field_pos: tuple, pos: tuple, map: list):
        current_number = map[field_pos[0]][field_pos[1]].number
        current_color = map[field_pos[0]][field_pos[1]].color
        if map[pos[0]][pos[1]].number == current_number:
            map[field_pos[0]][field_pos[1]]\
                .have_near_another_field = True
            if current_color == Color.BLACK:
                self.set_white_fields_around_black(field_pos, map)
            if map[pos[0]][pos[1]].color == Color.BLACK:
                if current_color == Color.BLACK:
                    self.set_white_fields_around_black(field_pos, map)
                else:
                    map[field_pos[0]][field_pos[1]].set_white()
            if current_color == Color.WHITE:
                self.set_black_color_in_pos(pos[0], pos[1], map)

    def check_three_in_row(self, pos: tuple, map: list):
        x, y = pos[0], pos[1]
        if x + 2 < len(map):
            if map[x + 2][y].number == map[x][y].number:
                if map[x + 1][y].number == map[x][y].number:
                    self.set_black_color_in_pos(x, y, map)
                    self.set_black_color_in_pos(x + 2, y, map)
                map[x + 1][y].set_white()

        if y + 2 < len(map):
            if map[x][y + 2].number == map[x][y].number:
                if map[x][y + 1].number == map[x][y].number:
                    self.set_black_color_in_pos(x, y, map)
                    self.set_black_color_in_pos(x, y + 2, map)
                map[x][y + 1].set_white()

    def set_black_color_in_pos(self, x: int, y: int, map: list):
        map[x][y].set_black()
        self.set_white_fields_around_black((x, y), map)

    @staticmethod
    def check_quad_middle(pos: tuple, map: list):
        black_field_count = 0
        white_chip_pos = None
        for direction in DIRECTIONS:
            x, y = direction[0] + pos[0], direction[1] + pos[1]
            if 0 <= x < len(map) and 0 <= y < len(map):
                if map[x][y].color == Color.BLACK:
                    black_field_count += 1
                if map[x][y].color == Color.GREY:
                    white_chip_pos = (x, y)
        if black_field_count == 3 and white_chip_pos is not None:
            map[white_chip_pos[0]][white_chip_pos[1]].set_white()
        if black_field_count == 2 and white_chip_pos is not None:
            if pos[0] == len(map) - 1 \
                    or pos[0] == 0 \
                    or pos[1] == len(map) - 1 \
                    or pos[1] == 0:
                map[white_chip_pos[0]][white_chip_pos[1]].set_white()

    def check_pair_isolation(self, pos: tuple, map: list):
        x, y = pos[0], pos[1]
        number = map[x][y].number
        for i in range(1, len(map) - 1):
            if map[x][y].color == Color.BLACK:
                self.set_white_fields_around_black((x, y), map)
                break
            else:
                if self.check_pair_fields(map, (x, y + i),
                                          (x, y + i + 1), number):
                    map[x][y].set_black()
                if self.check_pair_fields(map, (x, y - i),
                                          (x, y - i - 1), number):
                    map[x][y].set_black()
                if self.check_pair_fields(map, (x + i, y),
                                          (x + i + 1, y), number):
                    map[x][y].set_black()
                if self.check_pair_fields(map, (x - i, y),
                                          (x - i - 1, y), number):
                    map[x][y].set_black()

    def check_pair_fields(self, map: list, pos_1: tuple,
                          pos_2: tuple, number: int):
        if 0 <= pos_2[0] < len(map) and 0 <= pos_2[1] < len(map):
            if map[pos_1[0]][pos_1[1]].number \
                    == map[pos_2[0]][pos_2[1]].number == number:
                return True

    @staticmethod
    def set_white_fields_around_black(black_field_pos: tuple, map: []):
        for direction in DIRECTIONS:
            current_white_pos = (direction[0] + black_field_pos[0],
                                 direction[1] + black_field_pos[1])
            if 0 <= current_white_pos[0] < len(map) \
                    and 0 <= current_white_pos[1] < len(map):
                map[current_white_pos[0]][current_white_pos[1]].set_white()
