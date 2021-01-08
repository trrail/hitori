from hitori.hitori_game.logic.const import Color


class Field:
    def __init__(self, color: Color, number: int):
        self.color = color
        self.number = number
        self.have_near_another_field = False

    def change_color(self):
        colors = {Color.BLACK: self.set_grey,
                  Color.WHITE: self.set_black,
                  Color.GREY: self.set_white}
        colors[self.color]()

    def set_black(self):
        self.color = Color.BLACK

    def set_white(self):
        self.color = Color.WHITE

    def set_grey(self):
        self.color = Color.GREY

    def set_red(self):
        self.color = Color.RED
