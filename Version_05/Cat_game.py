#Juan Y Jamileth
# Fecha: Mayo de 2025
# Descripción: version 4 Juego del gato

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh
from Media import Background
from pygame.sprite import Group

from Version_04.Media import TurnImage


def run_game()->None:
    """
    Función principal.
    """
    #Inicia modulo pygame
    pygame.init()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background=Background()
    #Ciclo principal del juego

    #Se crea el objeto de marcador.
    marks = Group()

    turn_image = TurnImage()

    game_over=False

    while not game_over:
        game_over = game_event(marks, turn_image)
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen,clock,background, marks, turn_image)
        # Se cierran los recursos del juego
    pygame.quit()

if __name__ == '__main__':
    run_game()