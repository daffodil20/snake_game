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
snake.append([DIMENSION/2,DIMENSION/2])
direction = [0]
counter = 1
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
    if time.time()-snake_timer > 0.5*counter:
        if direction[counter-1] ==0:
            snake[counter-1][1]-=20
            snake[counter-1][1]=boundary(snake[counter-1][1])
        if direction[counter-1] ==1:
            snake[counter-1][0]+=20
            snake[counter-1][0]=boundary(snake[counter-1][0])
        if direction[counter-1] ==2:
            snake[counter-1][1]+=20
            snake[counter-1][1]=boundary(snake[counter-1][1])
        if direction[counter-1] ==3:
            snake[counter-1][0]-=20
            snake[counter-1][0]=boundary(snake[counter-1][0])
        if i!=0:
            direction[len(direction)-1-counter]=direction[len(direction)-2-counter]
        counter +=1
    
    if  time.time()-snake_timer > 0.5*(len(direction)):       
        snake_timer+=0.5*(len(direction))
        counter = 1

    #events triggered by keyboard 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print(snake)
            print(direction)
            if event.key == pygame.K_DOWN:
                dir=2
                # for part in snake:
                #     part[1] += 20
                #     part[1] = boundary(part[1])
                   
                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0][1] += 20
                snake[0][1] = boundary(snake[0][1])     

            if event.key == pygame.K_UP:
                dir=0
                # for part in snake:
                #     part[1] -= 20
                #     part[1] = boundary(part[1])
                 
                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0][1] -= 20
                snake[0][1] = boundary(snake[0][1])      

            if event.key == pygame.K_LEFT:
                dir=3
                # for part in snake:
                #     part[0] -= 20
                #     part[0] = boundary(part[0])
  
                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0][0] -= 20
                snake[0][0] = boundary(snake[0][0])     

            if event.key == pygame.K_RIGHT:
                dir=1
                # for part in snake:
                #     part[0] += 20
                #     part[0] = boundary(part[0])
 
                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0][0] += 20
                snake[0][0] = boundary(snake[0][0])      

            direction[0] = dir

    #eat food
    if food_x == snake[0][0] and food_y == snake[0][1]:
        l = len(snake)
        # snake.append([snake[len(snake)-1][0],snake[len(snake)-1][1]])
        new_l = len(snake)
        # if direction[len(direction)-1] == 0:
        #     snake[len(snake)-1][1]-=20
        # if direction[len(direction)-1] == 1:
        #     snake[len(snake)-1][0]+=20
        # if direction[len(direction)-1] == 2:
        #     snake[len(snake)-1][1]+=20
        # if direction[len(direction)-1] == 3:
        #     snake[len(snake)-1][0]-=20
        # direction.append(direction[len(direction)-1])

        if direction[len(direction)-1] == 0:
            tail_x = snake[len(snake)-1][0] 
            tail_y = snake[len(snake)-1][1]-20
        if direction[len(direction)-1] == 1:
            tail_x = snake[len(snake)-1][0]+20 
            tail_y = snake[len(snake)-1][1]
        if direction[len(direction)-1] == 2:
            tail_x = snake[len(snake)-1][0] 
            tail_y = snake[len(snake)-1][1]+20
        if direction[len(direction)-1] == 3:
            tail_x = snake[len(snake)-1][0]-20
            tail_y = snake[len(snake)-1][1]
        snake.append([tail_x, tail_y])
        direction.append(direction[len(direction)-1])
        
        food_x = int(DIMENSION*random()/20)*20
        food_y = int(DIMENSION*random()/20)*20
        point=0
        if new_l == l+20:
            point+=10

    # draw the snake
    for i in range(len(snake)):
        if i==0:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(snake[0][0],snake[0][1],20,20))
        else:
            pygame.draw.rect(screen,(0,0,255),pygame.Rect(snake[i][0],snake[i][1],20,20))
    # record the point

    # font=pygame.font.SysFont("Arial",36)
    # txtsurf=font.render(str(y),True,(255,255,255))
    # txtsurf=font.render(str(y).encode("utf-8").decode("utf-8"),True,(255,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(200, 200))

    pygame.display.update()
    
pygame.quit()
print("current score :",point)
