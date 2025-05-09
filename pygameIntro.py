'''
pygame intro
'''
import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))

circle_pos = (random.randint(50,1230), random.randint(50,670))
rect_pos = (random.randint(0,1230), random.randint(0,670), 50, 50)

font = pygame.font.Font(None, 30)

score = 0

def checkCircleCollision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    if math.sqrt(((mouse_pos[0] - circle_pos[0])**2) + ((mouse_pos[1] - circle_pos[1])**2)) <= 50:
        return True
    return False

def checkRectCollision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    if (mouse_pos[0] >= rect_pos[0]) and (mouse_pos[0] <= (rect_pos[0] + 50)):
        if (mouse_pos[1] >= rect_pos[1]) and (mouse_pos[1] <= (rect_pos[1] + 50)):
            return True
        return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if checkCircleCollision():
                    circle_pos = (random.randint(50,1230), random.randint(50,670))
                    score += 1
                #else:
                    #score -= 1
                if checkRectCollision():
                    rect_pos = (random.randint(0,1230), random.randint(0,670), 50, 50)
                    score += 1

    scoreObj = font.render(f'Score: {score}', True, 'black')


    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", circle_pos, 50)
    pygame.draw.rect(screen, "green", pygame.Rect(rect_pos))
    screen.blit(scoreObj, (50,50))

    pygame.display.update()
