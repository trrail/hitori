from enum import Enum

RECT_WIDTH_HEIGHT = 80
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
OPEN_WINDOW_SIZE = (500, 500)


class PreparedMaps(Enum):
    FIRST_MAP = 'resourses\\' + '1.txt'
    SECOND_MAP = 'resourses\\' + '2.txt'
    THIRD_MAP = 'resourses\\' + '3.txt'
    FOURTH_MAP = 'resourses\\' + '4.txt'
    FIFTH_MAP = 'resourses\\' + '5.txt'
    SIXTH_MAP = 'resourses\\' + '6.txt'
    SEVENTH_MAP = 'resourses\\' + '7.txt'


class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (96, 96, 96)
    RED = (189, 92, 92)
