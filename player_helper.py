import pygame
import constants_si

class Player:
    def __init__(self, image_path, x, y, width, height, speed_x):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, [width, height])
        self.speed_x = speed_x
        self.lasers = []
        self.expired_lasers = []
        self.attack_time_checker = pygame.time.get_ticks()
        self.attack_cooldown = 500

    def move_x(self):
        self.x += self.speed_x

    def handle_movement_input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_d]:
            self.speed_x = 0
        elif pressed_keys[pygame.K_a]:
            if self.check_screen_collision()[0] == False:
                self.speed_x = -5
            else:
                self.speed_x = 0
        elif pressed_keys[pygame.K_d]:
            if self.check_screen_collision()[1] == False:
                self.speed_x = 5
            else:
                self.speed_x = 0
        else:
            self.speed_x = 0
            
    def check_screen_collision(self):
        if self.x + self.width >= constants_si.SCREEN_X:
            return [False, True]
        elif self.x <= 0:
            return [True, False]
        else:
            return [False, False]
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.attack_time_checker > self.attack_cooldown:
            self.add_laser()
            self.attack_time_checker = pygame.time.get_ticks()
        
    def add_laser(self):
        laser = Laser(self.x + 48, self.y + 35, "green_laser.png", 5, 20, 10)
        self.lasers.append(laser)

    def draw_and_move_lasers(self, screen):
        for laser in self.lasers:
            if laser.y < 0:
                self.expired_lasers.append(laser)
            else:
                laser.draw(screen)
                laser.move()
        
    def handle_hits(self, enemies):
        for enemy in enemies:
            for laser in self.lasers:
                y_check = (enemy.y + enemy.height) >= laser.y and enemy.y <= laser.y
                if y_check == True:
                    x_check = enemy.x <= laser.x + laser.width and enemy.x + enemy.width >= laser.x
                    if x_check == True:
                        enemy.color = constants_si.RED
                        self.expired_lasers.append(laser)

    def remove_expired_lasers(self):
        for laser in self.expired_lasers:
            self.lasers.remove(laser)
        self.expired_lasers.clear()
            
class Laser:
    def __init__(self, x, y, laser_path, width, height, speed_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(laser_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, [width, height])
        self.speed_y = speed_y

    def move(self):
        self.y -= self.speed_y

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

class Enemy:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

