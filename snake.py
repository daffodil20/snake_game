import pygame
import time
from random import random
DIMENSION = 400

def boundary(a):
    if a>= DIMENSION:
        return DIMENSION-20
    if a<0:
        return 0
    return a

pygame.init()
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
running = True
snake=[]
food_timer = time.time()
snake_timer= time.time()
food_x= int(DIMENSION*random()/20)*20
food_y= int(DIMENSION*random()/20)*20
head = pygame.Rect(DIMENSION/2,DIMENSION/2,20,20)
snake.append(head)
direction = [0]
while running:
    screen.fill((0,0,0))
    # generate food every 6s
    if time.time()-food_timer > 12:
        food_x= int(DIMENSION*random()/20)*20
        food_y= int(DIMENSION*random()/20)*20
        food_timer+=12
    food = pygame.Rect(food_x,food_y,20,20)
    pygame.draw.rect(screen,(0,255,255),food)
   
    
    # snake automatic moves
    if time.time()-snake_timer > 0.5:
        for i in range(len(direction)):
            if direction[i] ==0:
                snake[i][1]-=20
                snake[i][1]=boundary(snake[i][1])
            if direction[i] ==1:
                snake[i][0]+=20
                snake[i][0]=boundary(snake[i][0])
            if direction[i] ==2:
                snake[i][1]+=20
                snake[i][1]=boundary(snake[i][1])
            if direction[i] ==3:
                snake[i][0]-=20
                snake[i][0]=boundary(snake[i][0])
        snake_timer+=0.5
        
    # update direction based on part ahead 
    for i in range(len(direction)):
        if i!=0:
            direction[i]=direction[i-1]

    #events triggered by keyboard       
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # y-=20
            # print("Down") 
            if event.key == pygame.K_DOWN:
                dir=2
                for body in snake:
                    body[1]+=20
                    body[1]=boundary(body[1])

            if event.key == pygame.K_UP:
                dir=0
                for body in snake:
                    body[1]-=20
                    body[1]=boundary(body[1])

            if event.key == pygame.K_LEFT:
                dir=3
                for body in snake:
                    body[0]-=20
                    body[0]=boundary(body[0])

            if event.key == pygame.K_RIGHT:
                dir=1
                for body in snake:
                    body[0]+=20
                    body[0]=boundary(body[0])

            direction[0]=dir
    
    #eat food
    if food_x == snake[0][0] and food_y == snake[0][1]:
    
        snake.append([snake[len(snake)-1][0],snake[len(snake)-1][1]])
        
        if direction[len(direction)-1]==0:
            snake[len(snake)-1][1]-=20
        if direction[len(direction)-1]==1:
            snake[len(snake)-1][0]+=20
        if direction[len(direction)-1]==2:
            snake[len(snake)-1][1]+=20
        if direction[len(direction)-1]==3:
            snake[len(snake)-1][0]-=20
        direction.append(direction[len(direction)-1])
        food_x= int(DIMENSION*random()/20)*20
        food_y= int(DIMENSION*random()/20)*20


    # draw the snake
    for i in range(len(snake)):
        if i==0:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(snake[0][0],snake[0][1],20,20))
        else:
            pygame.draw.rect(screen,(0,0,255),pygame.Rect(snake[i][0],snake[i][1],20,20))


    # font=pygame.font.SysFont("Arial",36)
    # txtsurf=font.render(str(y),True,(255,255,255))
    # txtsurf=font.render(str(y).encode("utf-8").decode("utf-8"),True,(255,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(200, 200))

    pygame.display.update()
    # x+=20
    # y+=1
    # snake[0][0]=snake[0][0] % DIMENSION
    # snake[0][1]=snake[0][1] % DIMENSION
    # time.sleep(0.1)
    
pygame.quit()