import pygame
import copy
import random
pygame.init()
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
isRunning = True
POS = [int(WIDTH/4+50), int(HEIGHT/4+20)]
POS1 = [int(WIDTH/4+30), int(HEIGHT/4+20)]
WAY = 1
RAN = []
RAN.append(POS)
RAN.append(POS1)
GENERATE_FOOD = True
FOOD =[random.randrange(int(WIDTH/4+20), int(WIDTH/2-20)), random.randrange(int(HEIGHT/4+20), int(HEIGHT/2-20)) ]
FOOD[0] -= FOOD[0]%10
FOOD[1] -= FOOD[1]%10
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and WAY != 3 and WAY != 1:
                WAY = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and WAY != 1 and WAY != 3:
                WAY = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and WAY != 2 and WAY != 0:
                WAY = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN  and WAY != 0 and WAY != 2:
                WAY = 2
            # if event.type == pygame.KEYUP and event.key == pygame.K_p :
            #     RAN.append(RAN[len(RAN)-1])
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, ((WIDTH/4), (HEIGHT/4), (WIDTH/2), (HEIGHT/2)), 1)
    for POINT in RAN:  
        pygame.draw.circle(window, WHITE, POINT, 10)
    if GENERATE_FOOD:
        pygame.draw.circle(window, ORANGE, FOOD, 10)
    if RAN[0][0] == FOOD[0] and RAN[0][1] == FOOD[1]:
        FOOD = [random.randrange(int(WIDTH/4+20), int(WIDTH/2-20)), random.randrange(int(HEIGHT/4+20), int(HEIGHT/2-20)) ]
        FOOD[0] -= FOOD[0]%10
        FOOD[1] -= FOOD[1]%10
        RAN.append(RAN[len(RAN)-1])
    OLDRAN = copy.deepcopy(RAN)
    for i in range(len(RAN)-1, 0, -1):
        RAN[i] = OLDRAN[i-1]
    if WAY == 1:
        RAN[0][0] += 10
    if WAY == 2:
        RAN[0][1] += 10
    if WAY == 3:
        RAN[0][0] -= 10
    if WAY == 0:
        RAN[0][1] -= 10
    for i in range(1, len(RAN) - 1) :
        if(RAN[0] == RAN[i]):
            isRunning = False
    if RAN[0][0] > (WIDTH/4)+(WIDTH/2) - 10 :
        isRunning = False
    if RAN[0][0] < (WIDTH/4) + 10:
        isRunning = False
    if RAN[0][1] < (HEIGHT/4) + 10:
        isRunning = False
    if RAN[0][1] > (HEIGHT/4)+(HEIGHT/2) - 10:
        isRunning = False
    clock.tick(10)
    pygame.display.flip()
pygame.quit()