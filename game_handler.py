import pygame
import constants_si

def create_screen(size):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(constants_si.SCREEN_TITLE)
    return screen