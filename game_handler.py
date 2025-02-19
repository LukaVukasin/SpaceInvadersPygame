import pygame
import constants_si
import player_helper

enemies = []

def load_level_1():
    for i in range(10):
        if i == 0:
            enemy = player_helper.Enemy(20, 20, 75, 75, "green_enemy.png", 3)
            enemies.append(enemy)
        else:
            enemy = player_helper.Enemy(enemies[i - 1].x + 100, 20 , 75, 75, "green_enemy.png", 3)
            enemies.append(enemy)

def remove_dead_enemies():
    enemies_to_remove = []
    for enemy in enemies:
        if enemy.alive == False:
            enemies_to_remove.append(enemy)
    
    for enemy in enemies_to_remove:
        enemies.remove(enemy)


def create_screen(size):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(constants_si.SCREEN_TITLE)
    return screen