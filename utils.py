import math
import numpy as np
import random
import pygame
import pygame.mixer
import time
from pygame.locals import *

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0 ,0)
width, height = 570, 726
center_x, center_y = width /2, height /2
screen = pygame.display.set_mode((width,height)) 
image = pygame.image.load(r'AI2_Assignment1_T3_2021.png')  

def display_player_with_ball(x, y):
    myfont = pygame.font.SysFont("monospace", 50)
    ball = myfont.render("Ball", 1, (255,255,0))
    screen.blit(ball, (x, y))

def refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4):
    screen.blit(image, (0, 0))
    draw_players(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)

def display_goal(distance):
    myfont = pygame.font.SysFont("monospace", 50)
    label = myfont.render("Goal", 1, (255,255,0))
    screen.blit(label, (100, 100))
    print(distance)
   

def detect_goal(gx2, gy2, distance):
    if gx2 in range(240, 340) and gy2 in range(0, 50):
        print('Goal')
        display_goal(distance)
      
def calc_distance(x1, y1, x2, y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def calc_min_dist(*argv):
    arguments = [x for x in argv]
    arguments_passed = len(arguments)
    distance = []
    for i in range(2, len(arguments),2):
        d = calc_distance(arguments[0], arguments[1], arguments[i], arguments[i+1])
        distance.append(d)
    min_dist_arg = np.argmin(distance)
    return min_dist_arg, distance[min_dist_arg]

def draw_players(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4):
    #center blue player
    pygame.draw.circle(screen, blue, [center_x, center_y+14], 17)
    #Red Goal Area
    pygame.draw.circle(screen, red, [gx1, gy1], 20)
    pygame.draw.circle(screen, blue, [gx2, gy2], 20)
    #Red Playing Area
    pygame.draw.circle(screen, blue, [rx1, ry1], 20)
    pygame.draw.circle(screen, red, [rx2, ry2], 20)
    pygame.draw.circle(screen, blue, [rx3, ry3], 20)
    pygame.draw.circle(screen, red, [rx4, ry4], 20)

def draw_ball(x, y):
    pygame.draw.circle(screen, black, [x, y], 10)

def generate_randomized_positions():
    gx1 = random.randint(100,450) 
    gy1 = random.randint(20,160)
    gx2 = random.randint(100,450) 
    gy2 = random.randint(20,160) 
    # Co-ordinates for ball
    bx = random.randint(50,520)
    by = random.randint(50,343)
    #players in red zone
    rx1 = random.randint(50,520)
    ry1 = random.randint(180, 343)
    rx2 = random.randint(50,520)
    ry2 = random.randint(180, 343)
    rx3 = random.randint(50,520)
    ry3 = random.randint(180, 343)
    rx4 = random.randint(50,520)
    ry4 = random.randint(180, 343)

    return gx1, gy1, gx2, gy2, bx, by, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4

