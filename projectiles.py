
import pygame

proyectiles = []

def crear(x, y, imagen):
    """
    Crea un proyectil con una imagen en la posición (x, y).
    """
    rect = pygame.Rect(
        x - imagen.get_width() // 2,
        y,
        imagen.get_width(),
        imagen.get_height()
    )
    proyectiles.append({"rect": rect, "speed": 7, "img": imagen})

def mover():
    '''Movimiento del proyectil'''
    for proyectil in proyectiles[:]:
        proyectil["rect"].y -= proyectil["speed"]
        if proyectil["rect"].bottom < 0:
            proyectiles.remove(proyectil)

def dibujar(screen):
    '''dibujo del proyectil en pantalla'''
    for proyectil in proyectiles:
        screen.blit(proyectil["img"], proyectil["rect"])
        
