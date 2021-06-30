# Dear future me, We both know I don't usually write comments on my code.
# but I have to write this time around.. this is the most complex game I've written since I started programming.
# alright, let's get started

# space invaders game by me written purely in python and one of it's module pygame
import pygame
import random
pygame.init()
width = 1000
height = 650
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('space_invaders')
red = (255, 0, 0)
green = (0, 255, 0)
text = pygame.font.SysFont("Helvetica", 20)
run = True


# player class
# I don't think I need to write comments on this class, It's pretty explanative on it's own 
# and besides, I expect future me to be smater than me
class Player:
    def __init__(self, vel, lives):
        self.x = 500
        self.y = 550
        self.vel = vel
        self.lives = lives
        self.head_x = self.x + 15
        self.head_y = self.y - 10
        self.bullets = []

    def create_player(self):
        self.head_x = self.x + 15
        self.head_y = self.y - 10
        pygame.draw.rect(win, green, (self.x, self.y, 40, 10))
        pygame.draw.rect(win, green, (self.head_x, self.head_y, 10, 10))

    def move_player(self):
        keys = pygame.key.get_pressed()
        if self.x > 0:
            if keys[pygame.K_LEFT]:
                self.x -= self.vel
        if self.x + 40 < 1000:
            if keys[pygame.K_RIGHT]:
                self.x += self.vel

    def hero_bullets(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet_pos = [self.head_x + 2, self.head_y - 5]
            if len(self.bullets) < 1:
                self.bullets.append(bullet_pos)
            elif len(self.bullets) >= 1:
                if self.head_y >= self.bullets[-1][1] + 100:
                    self.bullets.append(bullet_pos)

    def shoot(self):
        for bullet in self.bullets:
            pygame.draw.rect(win, green, (bullet[0], bullet[1], 5, 20))
            bullet[1] -= 10
            if bullet[1] <= 0:
                self.bullets.remove(bullet)

# Invader class
# now this is the class that needs explanation!
# To prevent future me from saying too much "what the fuck?".
class Invaders:
    def __init__(self):
        # the vertical speed of invaders
        self.vel_x = 5
        # the horizontal speed of invaders
        self.vel_y = 5
        self.width = 40
        self.height = 40
        self.row = -1
        self.back = 1
        self.check = []
        self.bullet_pos = []
        self.bullets = []
        self.dead_invaders = []
        # Invaders coordinates
        # the third number is for checking th 
        self.coordinates = [[[115, 20, 0], [185, 20, 1], [255, 20, 2], [325, 20, 3], [395, 20, 4], [465, 20, 5], [535, 20, 6], [605, 20, 7], [675, 20, 8], [745, 20, 9], [815, 20, 10]],
                            [[115, 80, 0], [185, 80, 1], [255, 80, 2], [325, 80, 3], [395, 80, 4], [465, 80, 5], [535, 80, 6], [605, 80, 7], [675, 80, 8], [745, 80, 9], [815, 80, 10]],
                            [[115, 140, 0], [185, 140, 1], [255, 140, 2], [325, 140, 3], [395, 140, 4], [465, 140, 5], [535, 140, 6], [605, 140, 7], [675, 140, 8], [745, 140, 9], [815, 140, 10]],
                            [[115, 200, 0], [185, 200, 1], [255, 200, 2], [325, 200, 3], [395, 200, 4], [465, 200, 5], [535, 200, 6], [605, 200, 7], [675, 200, 8], [745, 200, 9], [815, 200, 10]]]
                   
        self.check_left = []
        self.check_right = []

    def create_invaders(self):
        for c in self.coordinates:
            for pos in c:
                pygame.draw.rect(win, red, (pos[0], pos[1], self.width, self.height))

    def move_invaders(self):
        for coordinate in self.coordinates:
            if not coordinate:
                empty_row_pos = -(self.coordinates.index(coordinate) + 1)
                del self.check_left[empty_row_pos]
                del self.check_right[empty_row_pos]
                self.coordinates.remove(coordinate)
    
        rows = self.coordinates
        if len(self.coordinates) == 4:                  
            self.check_left = [rows[3][0][2], rows[2][0][2], rows[1][0][2], rows[0][0][2]]
            self.check_right = [rows[3][-1][2], rows[2][-1][2], rows[1][-1][2], rows[0][-1][2]]
        if len(self.coordinates) == 3:
            self.check_left = [rows[2][0][2], rows[1][0][2], rows[0][0][2]]
            self.check_right = [rows[2][-1][2], rows[1][-1][2], rows[0][-1][2]]
        if len(self.coordinates) == 2:          
            self.check_left = [rows[1][0][2], rows[0][0][2]]
            self.check_right = [rows[1][-1][2], rows[0][-1][2]]
        if len(self.coordinates) == 1:               
            self.check_left = [rows[0][0][2]]
            self.check_right = [rows[0][-1][2]]

        left_limit = -(self.check_left.index(min(self.check_left)) + 1)
        right_limit = -(self.check_right.index(max(self.check_right)) + 1)

        for coordinate in self.coordinates:
            for pos in coordinate:
                pos[0] += self.vel_x
                if self.coordinates[right_limit][-1][0] + self.width >= 1000:
                    pos[1] += self.vel_y    
                if self.coordinates[left_limit][0][0] == 0:
                    pos[1] += self.vel_y

        if self.coordinates[right_limit][-1][0] + self.width >= 1000:
            self.vel_x = -5
        if self.coordinates[left_limit][0][0] == 0:
            self.vel_x = 5
         
    def create_bullets(self):
        if len(self.coordinates) > 1:
            if len(self.coordinates[self.row]) == 11:
                self.bullet_pos = self.coordinates[self.row]
            if len(self.coordinates[-1]) < 11:
                for invader in self.dead_invaders:
                    for pos in self.coordinates[self.row - self.back]:
                        if pos[2] == invader:
                            self.check += [pos]
                            self.dead_invaders.remove(invader)
                self.bullet_pos = self.coordinates[self.row] + self.check
        

    def shoot_bullets(self):
        raw_bullet = random.choice(self.bullet_pos)
        bullet = raw_bullet.copy()
        if len(self.bullets) < 4:
            if len(self.bullets) < 1:
                self.bullets.append(bullet)
            if len(self.bullets) >= 1:
                if bullet[1] + 40 <= self.bullets[-1][1] and bullet[0] != self.bullets[-1][0]:
                    self.bullets.append(bullet)
        for bullet in self.bullets:
            pygame.draw.rect(win, red, (bullet[0]  + 20, bullet[1] + 20, 5, 20))
            bullet[1] += 10
            if bullet[1] + 20 >= 650:
                self.bullets.remove(bullet)

defender = Player(5, 3)
enemy = Invaders()
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((20, 20, 20))
    win.blit(text.render("LIVES: " + str(defender.lives), True, (0, 255, 0)), (930, 5))
    defender.create_player()
    defender.move_player()
    defender.hero_bullets()
    defender.shoot()
    enemy.create_invaders()
    enemy.move_invaders()
    enemy.create_bullets()
    enemy.shoot_bullets()

    for coord in enemy.coordinates:
        for e in coord:
            for b in defender.bullets:
                if b[0] in range(e[0], e[0]+40):
                    if b[1] <= e[1]:
                        if e in enemy.coordinates[enemy.row]:
                            enemy.dead_invaders.append(e[2])
                        coord.remove(e)
                        defender.bullets.remove(b)
    
    for shots in enemy.bullets:
        if shots[0] in range(defender.x, defender.x+40):
            if shots[1] >= defender.y:
                enemy.bullets.remove(shots)
                defender.lives -= 1
    
    pygame.display.update()

pygame.quit()
