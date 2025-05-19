# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 07 Juego del gato

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh,check_winner,game_over_screen
from Media import Background,TurnImage,Audio
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

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())

    #Se crea el objeto de marcador.
    marks = Group()

    turn_image = TurnImage()

    game_over=False
    result=''

    while not game_over:
        game_event(marks, turn_image,audio)
        # Se dibuja los elementos gráficos en la pantalla
        game_over,result=check_winner(marks)
        screen_refresh(screen,clock,background, marks, turn_image)

        # Se cierran los recursos del juego
    game_over_screen(audio,screen, clock, background, marks, turn_image, result)
    pygame.quit()

# Código a nivel de módulo.
if __name__ == '__main__':
    run_game()