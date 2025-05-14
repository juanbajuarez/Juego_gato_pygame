# Juan Y Jamileth
# Fecha: Mayo de 2025
# Descripción: version 4 Juego del gato
class Configurations:
    """ Clase que contiene todas las configuraciones del juego """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)              # Alto por ancho
    _game_title = "Juego del gato"          #Título del juego
    _background = (255, 100, 50)            #Fondo de la pantalla en RGB
    _fps = 8

    # Rutas de las imágenes utilizadas para las clases Background, SnakeBlock y Apple.

    _background_image_path = "../Media/background_image.png"

    _mark_size = (100, 100)
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

    _mark_x_path = "../Media/markX.png"
    _mark_o_path = "../Media/markO.png"

    # Métodos de acceso
    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para _screen_size
        :return: una tupla
        """
        return cls._screen_size

    @classmethod
    def get_mark_size(cls) -> tuple[int, int]:
        """
        Getter para _mark_size
        :return: una tupla
        """
        return cls._mark_size


    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        :return: una cadena
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """
        Getter para _background
        :return:
        """
        return cls._background

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
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

