# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 07 Juego del gato

import pygame

class Configurations:
    """ Clase que contiene todas las configuraciones del juego """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)              # Alto por ancho
    _game_title = "Juego del gato"          #Título del juego
    _fps = 8
    _game_over_screen_time = 5

    # Rutas de las imágenes utilizadas para las clases Background, mark0 y markx.
    _background_image_path = "../Media/background_image.png"
    _mark_x_path = "../Media/markX.png"
    _mark_o_path = "../Media/markO.png"

    #Marcadores de jugadores
    _mark_x_turn_path = "../Media/turnX.png"
    _mark_o_turn_path = "../Media/turnO.png"

    #Tamaño de las imagenes
    _mark_size = (100, 100)
    _mark_turn_image_size = (400, 200)

    #Rutas de las imágenes de los ganadores y los creditos
    _mark_win_x_path = "../Media/winX.png"
    _mark_win_o_path = "../Media/winO.png"
    _mark_draw_path = "../Media/draw.png"
    _credits_image_path = "../Media/credits.png"

    # Configuraciones de la música del juego.
    _music_volume = 0.25  # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).

    #Ruta de los audios del juego
    _music_path ="../Media/music.mp3"
    _keyboard_sound_path="../Media/keyboard_sound.mp3"
    _game_over_sound_path ="../Media/results_sound.mp3"


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



    # Métodos de acceso
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
    def get_background_image_path(cls) -> str:
        """Getter para _background_image_path."""
        return cls._background_image_path

    @classmethod
    def get_fps(cls) -> int:
        """Getter para _fps."""
        return cls._fps

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _game_over_screen_time.
        """
        return cls._game_over_screen_time

    @classmethod
    def get_cell_position(cls, cell_number: int) -> tuple[int, int]:
        """
        Getter para la posición de una celda específica.
        :param cell_number: Número de la casilla (1 a 9)
        :return: tupla con coordenadas (x, y)
        """
        return cls._cell_positions.get(cell_number, (0, 0))

    @classmethod
    def get_mark_x_path(cls) -> str:
        """
        Getter para _mark_x_path.
        """
        return cls._mark_x_path

    @classmethod
    def get_mark_o_path(cls) -> str:
        """
        Getter para _mark_o_path.
        """
        return cls._mark_o_path

    @classmethod
    def get_mark_x_turn_path(cls) -> str:
        """
        Getter para _mark_x_turn_path.
        """
        return cls._mark_x_turn_path

    @classmethod
    def get_mark_o_turn_path(cls) -> str:
        """
        Getter para _mark_o_turn_path.
        """
        return cls._mark_o_turn_path

    @classmethod
    def get_win_x_path(cls):
        """
        Getter para _mark_win_x_path.
        """
        return cls._mark_win_x_path

    @classmethod
    def get_win_o_path(cls):
        """
        Getter para _mark_win_o_path.
        """
        return cls._mark_win_o_path

    @classmethod
    def get_draw_path(cls):
        """
        Getter para _mark_draw_path.
        """
        return cls._mark_draw_path

    @classmethod
    def get_credits_image_path(cls):
        """
        Getter para _credits_image_path.
        """
        return cls._credits_image_path

    @classmethod
    def get_music_volume(cls) -> float:

        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_keyboard_sound_path(cls) -> str:
        """
        Getter para _keyboard_sound_path.
        """
        return cls._keyboard_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path


class ResultsImage:
    """
    Clase para mostrar los resultados del juego
    """
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



