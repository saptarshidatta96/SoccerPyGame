import pygame
import pygame.mixer
from pygame.locals import *
import random
import utils
from utils import *

pygame.init()  

done = False 
while not done: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    gx1, gy1, gx2, gy2, bx, by, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4 = generate_randomized_positions()
    refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
    pygame.time.Clock().tick(1)
    key = pygame.mouse.get_pressed()

    if key == (1,0,0):
        draw_ball(center_x, center_y)
        refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
        arg_min_dist = calc_min_dist(center_x, center_y, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
        if arg_min_dist == 0:
            draw_ball(rx1, ry1)
            new_arg_min = calc_min_dist(rx1, ry1, gx2, gy2)
            refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
            draw_ball(gx2, gy2)
            detect_goal(gx2, gy2)
                
        elif arg_min_dist == 1:
            draw_ball(rx2, ry2)
            new_arg_min = calc_min_dist(rx2, ry2, gx2, gy2)
            refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
            draw_ball(gx2, gy2)
            detect_goal(gx2, gy2)
        elif arg_min_dist == 2:
            draw_ball(rx3, ry3)
            new_arg_min = calc_min_dist(rx3, ry3, gx2, gy2)
            refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
            draw_ball(gx2, gy2)
            detect_goal(gx2, gy2)
        else:
            draw_ball(rx4, ry4)
            new_arg_min = calc_min_dist(rx4, ry4, gx2, gy2)
            refresh_screen(center_x, center_y, gx1, gy1, gx2, gy2, rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4)
            draw_ball(gx2, gy2)
            detect_goal(gx2, gy2)

    pygame.display.update()
    pygame.display.flip() 
