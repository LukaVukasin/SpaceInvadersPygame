import pygame
import player_helper
import game_handler
import constants_si
 
pygame.init()
 
screen = game_handler.create_screen([constants_si.SCREEN_X, constants_si.SCREEN_Y])

player = player_helper.Player("player.png", 600, 675, 100, 100, 0)

player_shooting = False

game_handler.load_level_1()
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_shooting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_shooting = True
    
    player.remove_expired_lasers()

    game_handler.remove_dead_enemies()

    for enemy in game_handler.enemies:
        enemy.check_image()

    player.handle_movement_input()

    player.move_x()

    player.handle_hits(game_handler.enemies)

    if player_shooting == True:
        player.shoot()
    
    screen.fill(constants_si.BACKGROUND_COLOR)

    for enemy in game_handler.enemies:
        enemy.draw(screen)

    player.draw_and_move_lasers(screen)
    
    screen.blit(player.image, [player.x, player.y])

    pygame.display.flip()

    clock.tick(constants_si.FRAME_RATE)

pygame.quit()