# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 07 Juego del gato

import pygame
from Configurations import Configurations
class Background:

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self):
        """

        """
        background_image_path=Configurations.get_background_image_path()
        self.image=pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size=Configurations.get_screen_size()
        self.image=pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()

    def blit (self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image,self.rect)


class TurnImage(pygame.sprite.Sprite):
    """
    Clase para mostrar la imagen del turno.
    """
    def __init__(self):
        super().__init__()
        self.image_x = pygame.image.load(Configurations.get_mark_x_turn_path())
        self.image_o = pygame.image.load(Configurations.get_mark_o_turn_path())

        self.image_x = pygame.transform.scale(self.image_x, Configurations.get_mark_turn_image_size())
        self.image_o = pygame.transform.scale(self.image_o, Configurations.get_mark_turn_image_size())

        self.image = self.image_x
        self.rect = self.image.get_rect()
        self.rect = Configurations.get_screen_turn_size()    # Se centra la imagen de turno

    def change_turn(self, current_player: str) -> None:
        if current_player == "X":
            self.image = self.image_x
        else:
            self.image = self.image_o

class ResultsImage:
    def __init__(self, result: str):
        if result == 'X':
            path = Configurations.get_win_x_path()
        elif result == 'O':
            path = Configurations.get_win_o_path()
        else:
            path = Configurations.get_draw_path()

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, Configurations.get_screen_status_size())
        self.rect = self.image.get_rect()
        self.rect.center = Configurations.get_position_status()


class CreditsImage:
    def __init__(self):
        path = Configurations.get_credits_image_path()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, Configurations.get_screen_credist_size())
        self.rect = self.image.get_rect()
        self.rect.center = Configurations.get_position_credits()

class Audio:
    def __init__(self):
        #Se carga la música del juego
        pygame.mixer.music.load(Configurations.get_music_path())


        # Se carga el sonido cuando se coloca una marca.
        self._keyboard_sound = pygame.mixer.Sound(Configurations.get_keyboard_sound_path())

        # Se carga el sonido cuando el juego ha terminado.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)  # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def play_game_over_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando el juego ha terminado.
        """
        self._game_over_sound.play()

    def play_keyboard_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando se pone una marca.
        """
        self._keyboard_sound.play()

