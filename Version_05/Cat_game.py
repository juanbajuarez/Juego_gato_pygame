#Juan Y Jamileth
# Fecha: Mayo de 2025
# Descripción: version 4 Juego del gato

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh
from Media import Background
from pygame.sprite import Group

from Media import TurnImage
from Version_05.Game_functionalities import check_winner, game_over_screen


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
    marks = pygame.sprite.Group()

    turn_image = TurnImage()

    game_over=False
    result = ''  # Inicia resultado vacío

    while not game_over:
        game_over = game_event(marks, turn_image)

        if not game_over:  # Solo si no se ha cerrado el juego
            game_over, result = check_winner(marks)
            screen_refresh(screen, clock, background, marks, turn_image)

    if result:  # Si terminó por victoria o empate
        game_over_screen(screen, clock, background, marks, turn_image, result)

    pygame.quit()

if __name__ == '__main__':
    run_game()