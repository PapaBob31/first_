
import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("snake")
x = 50
y = 50
vel_x = 10
vel_y = 0
snake_x = 0
snake_y = 0
last = []
change = False
current_pos = []
food_spawn = False
food_x = random.randrange(0, 500, 10)
food_y = random.randrange(0, 500, 10)
game_pause = False
game_start = True
snake_body = [[x, y]]
count = 0
pos = []
score = 0
run = True

while run:
    pygame.time.delay(100)
    pygame.time.set_timer(pygame.K_DOWN, 5000, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if game_start:
        black = win.fill((0, 0, 0))
        pygame.draw.rect(win, (123, 85, 225), (0, 0, 500, 15))
        pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))
        pygame.draw.rect(win, (255, 0, 0), (food_x, food_y, 10, 10))
        font = pygame.font.SysFont("verdana", 13)
        win.blit(font.render("SCORE:" + str(score), True, (255, 255, 255)), (420, 0))
        for body in snake_body[1:]:
            pygame.draw.rect(win, (0, 255, 0), (body[0], body[1], 10, 10))

        if game_pause:
            pygame.draw.rect(win, (255, 255, 255), (380, 0, 6, 15))
            pygame.draw.rect(win, (255, 255, 255), (390, 0, 6, 15))
            if keys[pygame.K_SPACE]:
                game_pause = False

        if not game_pause:
            pygame.draw.polygon(win, (255, 255, 255), ((380, 0), (395, 6), (380, 15)))
            x += vel_x
            y += vel_y
            if change:
                current_pos = [x - vel_x, y - vel_y, vel_x, vel_y]
                last.append(current_pos)
                change = False

            for body in snake_body[1:]:
                # pygame.draw.rect(win, (0, 255, 0), (body[0], body[1], 10, 10))
                body[0] += body[2]
                body[1] += body[3]
                if last:
                    for v in last:
                        if body[0] == v[0] and body[1] == v[1]:
                            body[2] = v[2]
                            body[3] = v[3]
                        if snake_body[-1][0] == v[0] and snake_body[-1][1] == v[1]:
                            last.remove(v)
                if body[2] != vel_x or body[3] != vel_y:
                    if y == body[1] + 10 and x == body[0]:
                        print("HIT")

            if food_spawn:
                pos = []
                food_x = random.randrange(0, 500, 10)
                food_y = random.randrange(20, 500, 10)
                food_spawn = False

            if len(snake_body) > 1:
                if vel_x > 0:
                    if keys[pygame.K_UP]:
                        change = True
                    elif keys[pygame.K_DOWN]:
                        change = True
                if vel_x < 0:
                    if keys[pygame.K_UP]:
                        change = True
                    elif keys[pygame.K_DOWN]:
                        change = True
                if vel_y > 0:
                    if keys[pygame.K_RIGHT]:
                        change = True
                    if keys[pygame.K_LEFT]:
                        change = True
                if vel_y < 0:
                    if keys[pygame.K_RIGHT]:
                        change = True
                    if keys[pygame.K_LEFT]:
                        change = True

            if vel_x > 0:
                vel_y = 0
                if keys[pygame.K_UP]:
                    vel_y = -10
                    vel_x = 0
                elif keys[pygame.K_DOWN]:
                    vel_y = 10
                    vel_x = 0
            if vel_x < 0:
                vel_y = 0
                if keys[pygame.K_UP]:
                    vel_y = -10
                    vel_x = 0
                elif keys[pygame.K_DOWN]:
                    vel_y = 10
                    vel_x = 0
            if vel_y > 0:
                vel_x = 0
                if keys[pygame.K_RIGHT]:
                    vel_x = 10
                    vel_y = 0
                if keys[pygame.K_LEFT]:
                    vel_x = -10
                    vel_y = 0
            if vel_y < 0:
                vel_x = 0
                if keys[pygame.K_RIGHT]:
                    vel_x = 10
                    vel_y = 0
                if keys[pygame.K_LEFT]:
                    vel_x = -10
                    vel_y = 0

            if food_x == x and food_y == y:
                score += 1
                food_spawn = True
                if len(snake_body) == 1:
                    snake_x = vel_x
                    snake_y = vel_y
                    pos = [x - (len(snake_body) * vel_x), y - (len(snake_body) * vel_y), snake_x, snake_y]
                elif len(snake_body) > 1:
                    snake_x = snake_body[-1][2]
                    snake_y = snake_body[-1][3]
                    pos = [snake_body[-1][0] - snake_body[-1][2], snake_body[-1][1] - snake_body[-1][3], snake_x, snake_y]
                snake_body.append(pos)
            if keys[pygame.K_p]:
                game_pause = True
                print("HIT_p")

    pygame.display.update()
pygame.quit()

