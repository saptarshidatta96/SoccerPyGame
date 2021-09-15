import pygame
import random
import math


pygame.init()  
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0 ,0)
width, height = 570, 726
center_x, center_y = width /2, height /2
screen = pygame.display.set_mode((width,height)) 
pygame.display.set_caption('Let’s Play Soccer')  
image = pygame.image.load(r'AI2_Assignment1_T3_2021.png')  
done = False  
  
while not done: 
    #gx = random.randint(-100,100) 
    #gy = random.randint(-300,-200)
    #co-ordinates for players at goal area 
    gx1 = random.randint(100,450) 
    gy1 = random.randint(50,160)
    gx2 = random.randint(100,450) 
    gy2 = random.randint(50,160) 
    # Co-ordinates for ball
    bx = random.randint(50,520)
    by = random.randint(50,343)
    #players in red zone
    rx = random.randint(-100,100)
    ry = random.randint(-150,0)
    screen.blit(image, (0, 0))
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    keys = pygame.key.get_pressed()
    pygame.time.Clock().tick(5)
    pygame.draw.circle(screen, (0,255, 0), [50, 50], 20)
    #ball
    pygame.draw.circle(screen, black, [center_x, center_y-4], 10)
    #center
    pygame.draw.circle(screen, blue, [center_x, center_y+14], 17)
    for key in keys:
        if keys[pygame.K_UP]:
            #ball
            pygame.draw.circle(screen, black, [bx, by], 10)
            #Red Goal Area
            #pygame.draw.circle(screen, blue, [center_x+gx/2, center_y+gy+gy/5], 17)
            #pygame.draw.circle(screen, red, [center_x+gx+gx/5, center_y+gy+gy/3], 17)
            pygame.draw.circle(screen, red, [gx1, gy1], 20)
            pygame.draw.circle(screen, blue, [gx2, gy2], 20)
            #Red Area
            pygame.draw.circle(screen, blue, [center_x+rx, center_y+ry], 17)
            pygame.draw.circle(screen, red, [center_x+rx/2, center_y+ry/5], 17)
            pygame.draw.circle(screen, blue, [center_x+rx+rx/7, center_y+ry/9], 17)
            pygame.draw.circle(screen, red, [center_x+rx+rx/6, center_y+ry+ry/5], 17)

    pygame.display.update()
    pygame.display.flip() 
