#Juan Y Jamileth
# Fecha: Mayo de 2025
# Descripción: version 4 Juego del gato

import pygame
from Configurations import Configurations
from Media import Background
from TicTacToeMark import TicTacToeMark


def game_event(marks: pygame.sprite.Group)->bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            key_to_cell = {
                pygame.K_q: 1, pygame.K_w: 2, pygame.K_e: 3,
                pygame.K_a: 4, pygame.K_s: 5, pygame.K_d: 6,
                pygame.K_z: 7, pygame.K_x: 8, pygame.K_c: 9,
            }
            if event.key in key_to_cell:
                new_mark = TicTacToeMark(key_to_cell[event.key])
                marks.add(new_mark)
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,
                   background:Background, marks: pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego
    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    marks.draw(screen)

    # Se actualiza la pantalla
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())