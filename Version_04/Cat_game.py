# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 04 Juego del gato

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh
from Media import Background
from pygame.sprite import Group



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

    marks = Group()

    game_over=False

    while not game_over:
        game_over = game_event(marks)
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen,clock,background, marks)
        # Se cierran los recursos del juego
    pygame.quit()

#Código a nivel de módulo.
if __name__ == '__main__':
    run_game()