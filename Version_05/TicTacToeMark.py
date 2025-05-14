# Juan y Jamileth
# Fecha: Mayo de 2025
# Descripción: Clase para las marcas del juego del gato

import pygame
from Configurations import Configurations

class TicTacToeMark(pygame.sprite.Sprite):
    """
    Clase que representa una marca en el tablero.
    Hereda de Sprite.
    """

    # Atributo de clase para manejar el turno del jugador
    turn = 'X'

    def __init__(self, cell_number: int):
        """
        Constructor que crea la marca según el turno actual
        y la posiciona en la casilla correspondiente.
        :param cell_number: número de la casilla (1 a 9)
        """
        super().__init__()
        self._cell_number = cell_number


        # Determinar imagen según el turno actual
        if TicTacToeMark.turn == 'X':
            image_path = Configurations.get_mark_x_path()
            TicTacToeMark.turn = 'O'
        else:
            image_path = Configurations.get_mark_o_path()
            TicTacToeMark.turn = 'X'

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, Configurations.get_mark_size())

        self.rect = self.image.get_rect()

        # Posicionar marca en el lugar correcto
        self.rect.center = Configurations.get_cell_position(cell_number)



    def get_cell_number(self) -> int:
        return self._cell_number

