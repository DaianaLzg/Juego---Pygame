import pygame
import os
import assets as a

def play_music():
    """
    Carga y reproduce música de fondo.
    """
    pygame.mixer.init()

    ruta_musica = os.path.join(a.MUSICA_DIR, "InGameMeteoro.mp3")

    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)