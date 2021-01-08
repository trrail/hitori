from hitori_game.logic.game import Game
from hitori_game.logic.const import PreparedMaps, Color


def test_change_field_color():
    game = Game()
    game.prepare_game(PreparedMaps.TEST_MAP)
    assert game.map.map[0][0].color == Color.GREY
    game.change_field_color((0, 0))
    assert game.map.map[0][0].color == Color.WHITE
    game.change_field_color((1, 1))
    game.change_field_color((1, 1))
    assert game.map.map[1][1].color == Color.BLACK


def test_solve():
    game = Game()
    game.prepare_game(PreparedMaps.TEST_MAP)
    game.solve()
    assert game.map.map[0][0].color == Color.BLACK


def test_check_player():
    game = Game()
    game.prepare_game(PreparedMaps.TEST_MAP)
    game.change_field_color((0, 0))
    game.check_player()
    assert game.map.map[0][0].color == Color.RED
