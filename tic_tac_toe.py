
import pygame
pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("tic tac toe")
run = True
draw = range(0, 600, 200)
points = ()
fill = True
font = pygame.font.SysFont('times new roman', 90)
o = False
x = False
player_one = ""
player_two = ""
check_2 = False
check_1 = False
game_start = False
not_picked = False
mouse_tap = 0
menu_pos = pygame.mouse.get_pos()
wait = True
game_over_x = False
game_over_o = False
restart = True
tie = False
display = False
game_o = [[(0, 0), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (2, 1)],
          [(0, 2), (1, 2), (2, 2)],
          [(0, 0), (0, 1), (0, 2)],
          [(1, 0), (1, 1), (1, 2)],
          [(2, 0), (2, 1), (2, 2)],
          [(0, 0), (1, 1), (2, 2)],
          [(2, 0), (1, 1), (0, 2)]]
game_x = [[(0, 0), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (2, 1)],
          [(0, 2), (1, 2), (2, 2)],
          [(0, 0), (0, 1), (0, 2)],
          [(1, 0), (1, 1), (1, 2)],
          [(2, 0), (2, 1), (2, 2)],
          [(0, 0), (1, 1), (2, 2)],
          [(2, 0), (1, 1), (0, 2)]]
coordinates = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]


def refresh():
    global game_o, game_x, coordinates, restart
    restart = True
    if restart:
        game_o = [[(0, 0), (1, 0), (2, 0)],
                  [(0, 1), (1, 1), (2, 1)],
                  [(0, 2), (1, 2), (2, 2)],
                  [(0, 0), (0, 1), (0, 2)],
                  [(1, 0), (1, 1), (1, 2)],
                  [(2, 0), (2, 1), (2, 2)],
                  [(0, 0), (1, 1), (2, 2)],
                  [(2, 0), (1, 1), (0, 2)]]
        game_x = [[(0, 0), (1, 0), (2, 0)],
                  [(0, 1), (1, 1), (2, 1)],
                  [(0, 2), (1, 2), (2, 2)],
                  [(0, 0), (0, 1), (0, 2)],
                  [(1, 0), (1, 1), (1, 2)],
                  [(2, 0), (2, 1), (2, 2)],
                  [(0, 0), (1, 1), (2, 2)],
                  [(2, 0), (1, 1), (0, 2)]]
        coordinates = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        restart = False


def constants():
    global points, fill, o, x, player_one, player_two, check_1, check_2, game_start, not_picked, mouse_tap, menu_pos, wait, game_over_x, game_over_o
    global game_o, tie
    global game_x, coordinates
    points = ()
    fill = True
    o = False
    x = False
    player_one = ""
    player_two = ""
    check_2 = False
    check_1 = False
    game_start = False
    not_picked = False
    mouse_tap = 0
    menu_pos = pygame.mouse.get_pos()
    wait = True
    game_over_x = False
    game_over_o = False
    tie = False
    refresh()


def game_over_msg():
    global display
    display = True
    if display:
        pygame.draw.rect(win, (255, 255, 255), (150, 100, 300, 100))
        pygame.draw.rect(win, (210, 210, 210), (150, 100, 300, 20))
        pygame.draw.rect(win, (0, 255, 0), (200, 160, 40, 25))
        pygame.draw.rect(win, (255, 0, 0), (350, 160, 40, 25))
        win.blit(font.render("YES!", True, (255, 0, 0)), (202, 162))
        win.blit(font.render("NO!", True, (0, 255, 0)), (352, 162))
        display = False


def paint():
    global fill
    if fill:
        win.fill((17, 13, 90))
        for i in draw:
            pygame.draw.rect(win, (220, 123, 45), (i, 0, 200, 600), 1)
            pygame.draw.rect(win, (220, 123, 45), (0, i, 600, 200), 1)
        fill = False


while run:
    keys = pygame.key.get_pressed()
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_BACKSPACE]:
            constants()
        if wait:
            game_start = False
            win.fill((0, 120, 190))
            # pygame.draw.rect(win, (13, 45, 225), (500, 500, 75, 25))
            pygame.draw.rect(win, (9, 200, 15), (7, 207, 190, 190))
            pygame.draw.rect(win, (200, 25, 15), (207, 207, 190, 190))
            pygame.draw.line(win, (200, 23, 15), (11, 214), (191, 391), 3)
            pygame.draw.line(win, (200, 23, 15), (191, 214), (11, 391), 3)
            pygame.draw.circle(win, (127, 200, 15), (300, 300), 90, 3)
            font = pygame.font.SysFont('Helvetica', 20)
            text = pygame.font.SysFont('Calibri(Body)', 100)
            menu = font.render("player one!, pick either X or O ", True, (100, 23, 98))
            player_1 = font.render("player one: " + player_one, True, (100, 23, 98))
            player_2 = font.render("player two: " + player_two, True, (100, 23, 98))
            Start = font.render("START!", True, (225, 103, 98))
            win.blit(text.render("TIC", False, (225, 0, 0)), (250, 3))
            win.blit(text.render("TAC", False, (0, 225, 0)), (250, 73))
            win.blit(text.render("TOE", False, (255, 0, 0)), (250, 147))
            win.blit(Start, (501, 501))
            win.blit(menu, (10, 130))
            win.blit(player_1, (10, 150))
            win.blit(player_2, (10, 170))
            if not_picked:
                win.blit(font.render("player 1 has not picked his choice!", True, (255, 0, 0)), (5, 500))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3):
                    menu_pos = pygame.mouse.get_pos()
                    coord = (menu_pos[0]//200, menu_pos[1]//200)
                    s_pos = (menu_pos[0]//50, menu_pos[1]//20)
                    if coord == (0, 1):
                        player_one = "X"
                        player_two = "O"
                        check_1 = True
                        clicked = True
                    elif coord == (1, 1):
                        player_one = "O"
                        player_two = "X"
                        check_2 = True
                        clicked = True
                    if s_pos == (10, 25):
                        if check_1 or check_2:
                            game_start = True
                            wait = False
                            mouse_tap = 1
                        else:
                            not_picked = True

        if game_start:
            paint()
            if not game_over_x and not game_over_o:
                if not coordinates:
                    tie = True
                    game_start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_tap += 1
                if pygame.mouse.get_pressed(num_buttons=3):
                    if mouse_tap > 2:
                        if check_1:
                            x = True
                            o = False
                            check_1 = False
                        if check_2:
                            o = True
                            x = False
                            check_2 = False
                        pos = pygame.mouse.get_pos()
                        points = (pos[0] // 200, pos[1] // 200)

                if o:
                    for c in coordinates:
                        if points == c:
                            pygame.draw.circle(win, (127, 200, 15), (((c[0] + 1) * 200) - 100, ((c[1] + 1) * 200) - 100), 90, 3)
                            o = False
                            x = True
                            coordinates.remove(c)
                            for g in game_o:
                                for e in g:
                                    if c == e:
                                        g.remove(e)
                                        if not game_o[0]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 100), (595, 100), 3)
                                        if not game_o[1]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 300), (595, 300), 3)
                                        if not game_o[2]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 500), (595, 500), 3)
                                        if not game_o[3]:
                                            pygame.draw.line(win, (225, 225, 225), (100, 5), (100, 595), 3)
                                        if not game_o[4]:
                                            pygame.draw.line(win, (225, 225, 225), (300, 5), (300, 595), 3)
                                        if not game_o[5]:
                                            pygame.draw.line(win, (225, 225, 225), (500, 5), (500, 595), 3)
                                        if not game_o[6]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 5), (595, 595), 3)
                                        if not game_o[7]:
                                            pygame.draw.line(win, (225, 225, 225), (595, 5), (5, 595), 3)
                                if not g:
                                    game_start = False
                                    game_over_o = True

                elif x:
                    for c in coordinates:
                        if points == c:
                            pygame.draw.line(win, (200, 23, 15), (((c[0] + 1) * 200) - 190, ((c[1] + 1) * 200) - 190), (((c[0] + 1) * 200) - 10, ((c[1] + 1) * 200) - 10,), 4)
                            pygame.draw.line(win, (200, 23, 15), (((c[0] + 1) * 200) - 10, ((c[1] + 1) * 200) - 190), (((c[0] + 1) * 200) - 190, ((c[1] + 1) * 200) - 10,), 4)
                            x = False
                            o = True
                            coordinates.remove(c)
                            for s in game_x:
                                for r in s:
                                    if c == r:
                                        s.remove(r)
                                        if not game_x[0]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 100), (595, 100), 3)
                                        if not game_x[1]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 300), (595, 300), 3)
                                        if not game_x[2]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 500), (595, 500), 3)
                                        if not game_x[3]:
                                            pygame.draw.line(win, (225, 225, 225), (100, 5), (100, 595), 3)
                                        if not game_x[4]:
                                            pygame.draw.line(win, (225, 225, 225), (300, 5), (300, 595), 3)
                                        if not game_x[5]:
                                            pygame.draw.line(win, (225, 225, 225), (500, 5), (500, 595), 3)
                                        if not game_x[6]:
                                            pygame.draw.line(win, (225, 225, 225), (5, 5), (595, 595), 3)
                                        if not game_x[7]:
                                            pygame.draw.line(win, (225, 225, 225), (595, 5), (5, 595), 3)
                                if not s:
                                    game_start = False
                                    game_over_x = True
        if game_over_o:
            game_over_msg()
            if player_one == "O":
                win.blit(font.render("player one won!", True, (255, 0, 0)), (155, 115))
                win.blit(font.render("would you like to play again", True, (255, 0, 0)),
                         (155, 130))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons=3):
                        mm = pygame.mouse.get_pos()
                        msg = (mm[0] // 50, mm[1] // 50)
                        if msg == (4, 3):
                            fill = True
                            game_start = True
                            game_over_o = False
                            check_2 = True
                            refresh()
                        elif msg == (7, 3):
                            game_over_o = False
                            constants()
            elif player_two == "O":
                win.blit(font.render("player two won!", True, (255, 0, 0)), (155, 115))
                win.blit(font.render("would you like to play again", True, (255, 0, 0)),
                         (155, 130))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons=3):
                        mm = pygame.mouse.get_pos()
                        msg = (mm[0] // 50, mm[1] // 50)
                        if msg == (4, 3):
                            fill = True
                            game_start = True
                            check_1 = True
                            refresh()
                            game_over_o = False
                        elif msg == (7, 3):
                            game_over_o = False
                            constants()

        if game_over_x:
            game_over_msg()
            if player_one == "X":
                win.blit(font.render("player one won!", True, (255, 0, 0)), (155, 115))
                win.blit(font.render("would you like to play again", True, (255, 0, 0)),
                         (155, 130))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons=3):
                        mm = pygame.mouse.get_pos()
                        msg = (mm[0] // 50, mm[1] // 50)
                        if msg == (4, 3):
                            fill = True
                            game_start = True
                            check_1 = True
                            refresh()
                            game_over_x = False
                        elif msg == (7, 3):
                            game_over_x = False
                            constants()
            elif player_two == "X":
                win.blit(font.render("player two won!", True, (255, 0, 0)), (155, 115))
                win.blit(font.render("would you like to play again", True, (255, 0, 0)),
                         (155, 130))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons=3):
                        mm = pygame.mouse.get_pos()
                        msg = (mm[0] // 50, mm[1] // 50)
                        if msg == (4, 3):
                            fill = True
                            game_start = True
                            check_2 = True
                            refresh()
                            game_over_x = False
                        elif msg == (7, 3):
                            game_over_x = False
                            constants()

        if tie:
            pygame.draw.rect(win, (255, 255, 255), (150, 100, 300, 100))
            pygame.draw.rect(win, (210, 210, 210), (150, 100, 300, 20))
            pygame.draw.rect(win, (0, 255, 0), (200, 160, 40, 25))
            pygame.draw.rect(win, (255, 0, 0), (350, 160, 40, 25))
            win.blit(font.render("Nobody won!, it was a tie!", True, (255, 0, 0)), (155, 115))
            win.blit(font.render("would you like to play again?", True, (255, 0, 0)), (155, 130))
            win.blit(font.render("YES!", True, (255, 0, 0)), (202, 162))
            win.blit(font.render("NO!", True, (0, 255, 0)), (352, 162))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3):
                    mm = pygame.mouse.get_pos()
                    msg = (mm[0] // 50, mm[1] // 50)
                    if msg == (4, 3):
                        tie = False
                        mouse_tap = 1
                        fill = True
                        game_start = True
                        refresh()
                    elif msg == (7, 3):
                        constants()

    # yes = (4, 3)
    # no = (7, 3)
    pygame.display.update()
pygame.quit()

