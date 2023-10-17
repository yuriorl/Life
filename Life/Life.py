import pygame
from pygame.locals import *
import time

pygame.init()
t0 = time.time()

fonts = pygame.font.get_fonts() #шрифты



trigger = 30
width = 720
height = 720
grid_num = 24
screen = pygame.display.set_mode((width,height))
GRID = []
wstep = width/grid_num
hstep = height/grid_num
for i in range(0,grid_num):
    for k in range(0,grid_num):
        GRID.append([[i*wstep,(i+1)*wstep],[k*hstep,(k+1)*hstep]])


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
MY = (150,150,255)




key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

def Create_Grid():
    for i in range(0,grid_num):
        for j in range(0,grid_num):
            pygame.draw.rect(screen, (5,5,5), (wstep*i, hstep*j, width/grid_num, height / grid_num), 1)
    pygame.display.update()
def Get_square(x):
    for i in GRID:
        if (x[0] > i[0][0] and x[0] < i[0][1]) and (x[1] > i[1][0] and x[1] < i[1][1]): # (координата x вернего левого угла, y, ширина, высота)
            return i
def back_ground(messages):
    screen.fill(background)
    pygame.display.update()
    Create_Grid()
    for i in squares_gotten:
        screen.fill(MY, ((i[0][0], i[1][0]), (wstep, hstep)))
    message1 = messages[0]
    message2 = messages[1]
    message3 = messages[2]
    manual = messages[3]
    text1 = font.render(message1, True, MY)
    text2 = font.render(message2, True, RED)
    text3 = font.render(message3, True, RED)
    help_button = font.render(manual, True, MY)
    screen.blit(text1, (200, 200))
    screen.blit(text2, (250, 150))
    screen.blit(text3, (250, 100))
    screen.blit(help_button, (10, 600))
taps = 0
squares_gotten = []
caption = "ТипаПрограммист пишу игру <<Жизнь>>"
pygame.display.set_caption(caption)
background = WHITE
screen.fill(background)
Create_Grid()
pygame.display.update()
font = pygame.font.SysFont('rage.ttf', 36)
message1 = "Welcome to the Life game!"
message2 = ""
message3 = ""
manual = "Press h for help"
messages = [message1,message2,message3,manual]
back_ground(messages)
running = True
while running:

    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                screen.fill(background)
                pygame.display.update()
                Create_Grid()
            if event.key == K_h:
                taps += 1
                if taps%2 == 0:

                    message1 = ""
                    message2 = ""
                    message3 = ""
                    manual = "Press h for help"
                    messages = [message1, message2, message3, manual]
                    back_ground(messages)
                else:
                    message1 = ""
                    message2 = ""
                    message3 = ""
                    manual = "Tap - choose a cell; ENTER - start; SPACE - abort; ESC - exit"
                    messages = [message1, message2, message3, manual]
                    back_ground(messages)
            if event.key == K_SPACE:
                screen.fill(background)
                Create_Grid()
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RETURN: #K_RETURN это ENTER
                message1 = ""
                message2 = "Life has begun"
                message3 = ""
                manual = ""
                messages = [message1, message2, message3, manual]
                back_ground(messages)
                print("Жизнь началась")
                playing = True
                counter = 0
                lifecells = []
                ALIVE = MY
                DEAD = background
                print("squares_gotten:"+str(len(squares_gotten)))
                for i in GRID:
                    if screen.get_at((int(i[0][0]+wstep/2), int(i[1][0] + hstep/2))) == MY:
                        lifecells.append(i)
                squares_gotten = lifecells

                while playing:

                    life = 0
                    cells_to_die = []
                    cells_to_live = []
                    for i in GRID:
                        if int(i[0][0]-wstep/2) < 0 and int(i[1][0] - hstep / 2) > 0 and int(i[1][0] + 3 * hstep / 2) < height:
                            life = [screen.get_at((int(i[0][0]+wstep/2), int(i[1][0] - hstep/2))),
                                    screen.get_at((int(i[0][0]+ 3*wstep/2), int(i[1][0] - hstep/2))),
                                    screen.get_at((int(i[0][0]+ 3*wstep/2), int(i[1][0] + hstep/2))),
                                    screen.get_at((int(i[0][0]+ 3*wstep/2), int(i[1][0] + 3*hstep/2))),
                                    screen.get_at((int(i[0][0]+ wstep/2), int(i[1][0] + 3*hstep/2)))].count(ALIVE)
                        elif int(i[1][0] - hstep / 2) < 0 and int(i[0][0]-wstep/2) > 0 and int(i[0][0] + 3 * wstep / 2) < width:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + 3 * hstep / 2)))].count(ALIVE)
                        elif int(i[0][0] + 3 * wstep / 2) > width and int(i[1][0] - hstep / 2) > 0 and int(i[1][0] + 3 * hstep / 2) < height:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + 3 * hstep / 2)))].count(ALIVE)
                        elif int(i[1][0] + 3 * hstep / 2) > height and int(i[0][0]-wstep/2) > 0 and int(i[0][0] + 3 * wstep / 2) < width:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + hstep / 2)))].count(ALIVE)
                        elif int(i[0][0]-wstep/2) < 0 and int(i[1][0] - hstep / 2) < 0:
                            life = [screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] + 3 * hstep / 2)))].count(ALIVE)
                        elif int(i[0][0] - wstep / 2) < 0 and int(i[1][0] + 3 * hstep / 2) > height:
                            life = [screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + hstep / 2)))].count(ALIVE)
                        elif int(i[0][0] + 3 * wstep / 2) > width and int(i[1][0] - hstep / 2) < 0:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] + 1 * wstep / 2), int(i[1][0] + 3*hstep / 2))),
                                    screen.get_at((int(i[0][0] - 1 * wstep / 2), int(i[1][0] + 3*hstep / 2)))].count(ALIVE)
                        elif int(i[0][0] + 3 * wstep / 2) > width and int(i[1][0] + 3 * hstep / 2) > height:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] - hstep / 2)))].count(ALIVE)
                        else:
                            life = [screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] - hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + hstep / 2))),
                                    screen.get_at((int(i[0][0] + 3 * wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] + 3 * hstep / 2))),
                                    screen.get_at((int(i[0][0] - wstep / 2), int(i[1][0] + 3 * hstep / 2)))].count(ALIVE)
                        if screen.get_at((int(i[0][0]+ wstep/2), int(i[1][0] + hstep/2))) == ALIVE and (life < 2 or life > 4):
                            cells_to_die.append(i) #screen.fill(DEAD, ((i[0][0], i[1][0]), (wstep, hstep)))
                        if screen.get_at((int(i[0][0]+ wstep/2), int(i[1][0] + hstep/2))) == DEAD and life == 3:
                            cells_to_live.append(i) #screen.fill(ALIVE, ((i[0][0], i[1][0]), (wstep, hstep)))


                    for i in cells_to_die:
                        screen.fill(DEAD, ((i[0][0], i[1][0]), (wstep, hstep)))
                    for i in cells_to_live:
                        screen.fill(ALIVE, ((i[0][0], i[1][0]), (wstep, hstep)))
                    lifenumber1 = len(lifecells)
                    lifecells = []

                    for i in GRID:
                        if screen.get_at((int(i[0][0] + wstep / 2), int(i[1][0] + hstep / 2))) == ALIVE:
                            lifecells.append(i)
                    squares_gotten = lifecells

                    Create_Grid()
                    time.sleep(0.25)
                    lifenumber2 = len(lifecells)

                    if lifenumber1 == lifenumber2:
                        counter+=1
                    else:
                        counter = 0



                    print("Живых клеток: " + str(lifenumber2))
                    message1 = ""
                    message2 = "Life lives!"
                    message3 = str("Alive cells:" + str(lifenumber2))
                    manual = ""
                    messages = [message1, message2, message3, manual]
                    back_ground(messages)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_SPACE:
                                playing = False
                                squares_gotten = []
                                message1 = ""
                                message2 = "Life has been aborted"
                                message3 = ""
                                manual = ""
                                messages = [message1, message2, message3, manual]
                                back_ground(messages)

                    if len(lifecells) == 0:
                        playing = False
                        squares_gotten = []
                        message1 = ""
                        message2 = "Life is over"
                        message3 = ""
                        manual = ""
                        messages = [message1, message2, message3, manual]
                        back_ground(messages)

                    if counter == trigger:
                        playing = False
                        squares_gotten = []
                        message1 = ""
                        message2 = "Life is infinite"
                        message3 = ""
                        manual = ""
                        messages = [message1, message2, message3, manual]
                        back_ground(messages)

                screen.fill(background)
                Create_Grid()
                back_ground(messages)



        if event.type == MOUSEBUTTONDOWN:
            message1 = "Welcome to the Life game!"
            message2 = ""
            message3 = ""
            manual = "Press h for help"
            messages = [message1, message2, message3, manual]
            back_ground(messages)
            i = Get_square(event.pos)
            squares_gotten.append(i)
            for i in squares_gotten:
                screen.fill(MY, ((i[0][0], i[1][0]), (wstep, hstep)))
            print("squares_gotten:" + str(len(squares_gotten)))
            #print(screen.get_at((int(i[0][0]+wstep/2), int(i[1][0] + hstep/2))))
            #print(event.pos)
            pygame.display.update()
            Create_Grid()


        if event.type == pygame.QUIT:
            running = False

pygame.quit()