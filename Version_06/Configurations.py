# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 06 Juego del gato

import pygame

class Configurations:
    """ Clase que contiene todas las configuraciones del juego """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)              # Alto por ancho
    _game_title = "Juego del gato"          #Título del juego
    _fps = 8
    _game_over_screen_time = 5
    _screen_credist_size = (400, 100)
    _position_credits = (650, 650)
    _position_status = (640, 360)
    _screen_status_size = (400, 400)
    _screen_turn_size = (450, 50)

    # Rutas de las imágenes utilizadas para las clases Background, mark0 y markx.
    _background_image_path = "../Media/background_image.png"
    _mark_x_path = "../Media/markX.png"
    _mark_o_path = "../Media/markO.png"

    #Marcadores de jugadores
    _mark_x_turn_path = "../Media/turnX.png"
    _mark_o_turn_path = "../Media/turnO.png"

    _mark_size = (100, 100)
    _mark_turn_image_size = (400, 200)

    _mark_win_x_path = "../Media/winX.png"
    _mark_win_o_path = "../Media/winO.png"
    _mark_draw_path = "../Media/draw.png"
    _credits_image_path = "../Media/credits.png"

    # Agregando las celdas.
    _cell_positions = {
        1:(500, 310),
        2:(640, 310),
        3:(775, 310),

        4:(500, 450),
        5:(640, 450),
        6:(775, 450),

        7:(500, 570),
        8:(640, 570),
        9:(775, 570)
    }
    _time_wait = 500


    # Métodos de acceso

    @classmethod
    def get_time_wait(cls) -> int:
        """Getter para _time_wait."""
        return cls._time_wait

    @classmethod
    def get_screen_turn_size(cls) -> tuple[int, int]:
        """Getter para _screen_turn_size"""
        return cls._screen_turn_size

    @classmethod
    def get_screen_status_size(cls) -> tuple[int, int]:
        """Getter para _screen_status_size"""
        return cls._screen_status_size

    @classmethod
    def get_screen_credist_size(cls) -> tuple[int, int]:
        """Getter para _screen_credist_size"""
        return cls._screen_credist_size

    @classmethod
    def get_position_status(cls) -> tuple[int, int]:
        """Getter para _position_status"""
        return cls._position_status

    @classmethod
    def get_position_credits(cls) -> tuple[int, int]:
        """Getter para _position_credits"""
        return cls._position_credits

    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """Getter para _screen_size"""
        return cls._screen_size

    @classmethod
    def get_mark_size(cls) -> tuple[int, int]:
        """Getter para _mark_size"""
        return cls._mark_size

    @classmethod
    def get_mark_turn_image_size(cls) -> tuple[int, int]:
        """Getter para _mark_turn_image_size"""
        return cls._mark_turn_image_size


    @classmethod
    def get_game_title(cls)->str:
        """Getter para _game_title"""
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """Getter para _background"""
        return cls._background

    @classmethod
    def get_background_image_path(cls) -> str:
        """Getter para _background_image_path."""
        return cls._background_image_path

    @classmethod
    def get_fps(cls) -> int:
        """Getter para _fps."""
        return cls._fps

    @classmethod
    def get_cell_position(cls, cell_number: int) -> tuple[int, int]:
        """
        Getter para la posición de una celda específica.
        :param cell_number: número de la casilla (1 a 9)
        :return: tupla con coordenadas (x, y)
        """
        return cls._cell_positions.get(cell_number, (0, 0))

    @classmethod
    def get_mark_x_path(cls) -> str:
        return cls._mark_x_path

    @classmethod
    def get_mark_o_path(cls) -> str:
        return cls._mark_o_path

    @classmethod
    def get_mark_x_turn_path(cls) -> str:
        return cls._mark_x_turn_path

    @classmethod
    def get_mark_o_turn_path(cls) -> str:
        return cls._mark_o_turn_path

    @classmethod
    def get_win_x_path(cls):
        return cls._mark_win_x_path

    @classmethod
    def get_win_o_path(cls):
        return cls._mark_win_o_path

    @classmethod
    def get_draw_path(cls):
        return cls._mark_draw_path

    @classmethod
    def get_credits_image_path(cls):
        return cls._credits_image_path


class ResultsImage:
    def __init__(self, result: str):
        if result == 'X':
            path = Configurations.get_win_x_path()
        elif result == 'O':
            path = Configurations.get_win_o_path()
        else:
            path = Configurations.get_draw_path()

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)



