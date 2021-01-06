import pygame
from hitori_game.logic.game import Game
from hitori_game.logic.const import PreparedMaps,\
    RECT_WIDTH_HEIGHT, OPEN_WINDOW_SIZE


class Window:
    def __init__(self):
        self.current_condition = self.open_menu
        self.screen_size = OPEN_WINDOW_SIZE
        self.screen = pygame.display.set_mode(self.screen_size)
        self.game = Game()

    def start(self) -> None:
        pygame.init()
        window_is_open = True
        while window_is_open:
            self.current_condition()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_is_open = False
            pygame.display.update()
        pygame.quit()

    def open_menu(self) -> None:
        self.set_open_menu_settings()
        self.print_text("Press button from 1 to 7 to choose level",
                        (25, 100), 34)
        if pygame.key.get_pressed()[pygame.K_1]:
            self.game.prepare_game(PreparedMaps.FIRST_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_2]:
            self.game.prepare_game(PreparedMaps.SECOND_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_3]:
            self.game.prepare_game(PreparedMaps.THIRD_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_4]:
            self.game.prepare_game(PreparedMaps.FOURTH_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_5]:
            self.game.prepare_game(PreparedMaps.FIFTH_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_6]:
            self.game.prepare_game(PreparedMaps.SIXTH_MAP)
            self.current_condition = self.game_screen
        if pygame.key.get_pressed()[pygame.K_7]:
            self.game.prepare_game(PreparedMaps.SEVENTH_MAP)
            self.current_condition = self.game_screen

    def game_screen(self):
        self.reset_game_screen(len(self.game.map.map))
        self.draw_rectangles()
        if pygame.mouse.get_pressed(3)[0]:
            pygame.time.wait(100)
            map_pos = self.define_rect(pygame.mouse.get_pos())
            if map_pos is not None:
                self.game.change_field_color(map_pos)
        if pygame.key.get_pressed()[pygame.K_s]:
            pygame.time.wait(50)
            self.game.solve()
        if pygame.key.get_pressed()[pygame.K_m]:
            pygame.time.wait(50)
            self.game.reset()
            self.current_condition = self.open_menu
        if pygame.key.get_pressed()[pygame.K_c]:
            pygame.time.wait(50)
            self.game.check_player()

    def print_text(self, message: str, position: tuple, font: int) -> None:
        text_stile = pygame.font.Font(None, font)
        text = text_stile.render(message, True, (200, 200, 200))
        self.screen.blit(text, position)

    def reset_game_screen(self, size):
        self.screen_size = (size * RECT_WIDTH_HEIGHT,
                            size * RECT_WIDTH_HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_size)
        surface = pygame.Surface(self.screen_size)
        surface.fill((255, 165, 0))
        self.screen.blit(surface, (0, 0))

    def set_open_menu_settings(self):
        self.screen_size = OPEN_WINDOW_SIZE
        self.screen = pygame.display.set_mode(self.screen_size)
        surface = pygame.Surface(self.screen_size)
        surface.fill((255, 165, 0))
        self.screen.blit(surface, (0, 0))

    def draw_rectangles(self):
        size = len(self.game.map.map)
        for x in range(size):
            for y in range(size):
                pygame.draw.rect(self.screen,
                                 self.game.map.map[x][y].color.value,
                                 (x * RECT_WIDTH_HEIGHT,
                                  y * RECT_WIDTH_HEIGHT,
                                  RECT_WIDTH_HEIGHT, RECT_WIDTH_HEIGHT))
                self.print_text(str(self.game.map.map[x][y].number),
                                (x * RECT_WIDTH_HEIGHT + 30,
                                 y * RECT_WIDTH_HEIGHT + 30),
                                50)

    def define_rect(self, mouse_pos: tuple) -> tuple:
        if 0 <= mouse_pos[0] <= self.screen_size[0] \
                and 0 <= mouse_pos[1] <= self.screen_size[1]:
            return mouse_pos[0] // RECT_WIDTH_HEIGHT,\
                   mouse_pos[1] // RECT_WIDTH_HEIGHT
