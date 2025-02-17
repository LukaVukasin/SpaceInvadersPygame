import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
size = (1200, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Space Invaders clone")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()