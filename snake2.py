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

food_timer = time.time()
snake_timer= time.time()
# head_x= int(DIMENSION*random()/20)*20
# head_y= int(DIMENSION*random()/20)*20
# head = Unit(head_x,head_y)
# snake.append([DIMENSION/2,DIMENSION/2])
direction = [0]
# the value of delay_counter increases when snake eat food
delay_counter = 1

class Unit:
    x=0
    y=0
    def __init__(self,food_x,food_y) -> None:
        self.x=food_x
        self.y=food_y
snake=[]
head_x= int(DIMENSION*random()/20)*20
head_y= int(DIMENSION*random()/20)*20
head = Unit(head_x,head_y)
snake.append(head)

foods=[]
for i in range(100):
    food_x= int(DIMENSION*random()/20)*20
    food_y= int(DIMENSION*random()/20)*20
    food_object = Unit(food_x,food_y)
    foods.append(food_object)
    # print(food_x,food_y)
# class Food:delay_counter +=1
#     food_loc = 
current_food=0
while running:
    screen.fill((0,0,0))
    # generate food every 6s
    
    if time.time()-food_timer > 12 and current_food<100:
        current_food += 1
        draw_food = pygame.Rect(foods[current_food].x,foods[current_food].y,20,20)
        pygame.draw.rect(screen,(0,255,255),draw_food)
        
        food_timer += 12
        # print(foods[current_food].x,foods[current_food].y)
        # i += 1current_food
    else:
        draw_food = pygame.Rect(foods[current_food].x,foods[current_food].y,20,20)
        pygame.draw.rect(screen,(0,255,255),draw_food)
        # food_timer += 12
        # i += 1
    
# food_array=[food_x,food_y]

    # snake automatic moves
    if time.time()-snake_timer > 0.5*delay_counter:
        for i in range(len(snake)):
            
        # judge the direction of the moving parts
            if direction[i] == 0:
                snake[i].x -= 20
                snake[i].x = boundary(snake[i].x)
            if direction[i] == 1:
                snake[i].y += 20
                snake[i].y = boundary(snake[i].y)
            if direction[i] == 2:
                snake[i].y += 20
                snake[i].y = boundary(snake[i].y)
            if direction[i] == 3:
                snake[i].x -= 20
                snake[i].x = boundary(snake[i].x)
        # the direction of latter is the same as its front one
            
            if len(direction) > 1 and i > 0:
                direction[i] = direction[i-1]
                snake_timer += 0.5*delay_counter
        # if len(direction) > 1:
        #     direction[len(direction)-delay_counter] = direction[len(direction)-delay_counter-1]
        # snake_timer += 0.5*delay_counter
        # delay_counter += 1
    
    if  time.time()-snake_timer > 0.5*(len(direction)):
        snake_timer = time.time()
        delay_counter = 1
    # print(snake[0].x,snake[0].y)
    #events triggered by keyboard 
    for event in pygame.event.get():
        # print(direction)
        if event.type ==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # print(snake)
            # print(direction)
            if event.key == pygame.K_DOWN:
                dir=2
                # for part in snake:
                #     part[1] += 20
                #     part[1] = boundary(part[1])

                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0].y += 20
                snake[0].y = boundary(snake[0].y)    

            if event.key == pygame.K_UP:
                dir=0
                # for part in snake:
                #     part[1] -= 20
                #     part[1] = boundary(part[1])

                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0].y -= 20
                snake[0].y = boundary(snake[0].y)      
                # print(snake[0].x,snake[0].y)
            if event.key == pygame.K_LEFT:
                dir=3
                # for part in snake:
                #     part[0] -= 20
                #     part[0] = boundary(part[0])

                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0].x -= 20
                snake[0].x = boundary(snake[0].x)     

            if event.key == pygame.K_RIGHT:
                dir=1
                # for part in snake:
                #     part[0] += 20
                #     part[0] = boundary(part[0])

                # for i in range(len(snake)-1):
                #     snake[len(snake)-1-i]=snake[len(snake)-2-i]
                snake[0].x += 20
                snake[0].x = boundary(snake[0].x)      

            direction[0] = dir
            print(direction[0])
            # if time.time()-snake_timer > 0.5*delay_counter:
            #     for i in range(len(snake)):
            #         if len(direction) > 1 and i > 0:
            #             direction[i] = direction[i-1]
            #             snake_timer += 0.5*delay_counter
            #     #eat food
    
    if foods[current_food].x == snake[0].x and foods[current_food].y == snake[0].y:
        # l = len(snake)
        # # snake.append([snake[len(snake)-1][0],snake[len(snake)-1][1]])
        # new_l = len(snake)
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
            tail_x = snake[len(snake)-1].x
            tail_y = snake[len(snake)-1].y-20
        if direction[len(direction)-1] == 1:
            tail_x = snake[len(snake)-1].x+20 
            tail_y = snake[len(snake)-1].y
        if direction[len(direction)-1] == 2:
            tail_x = snake[len(snake)-1].x
            tail_y = snake[len(snake)-1].y+20
        if direction[len(direction)-1] == 3:
            tail_x = snake[len(snake)-1].x-20
            tail_y = snake[len(snake)-1].y
        # snake_object = unit(tail_x,tail_y)
        # snake.append([tail_x, tail_y])
        foods[current_food].x=tail_x
        foods[current_food].y=tail_y
        # snake_object = Unit(tail_x,tail_y)
        snake.append(foods[current_food])
        foods.pop(current_food)
        direction.append(direction[len(direction)-1])
        # delay_counter +=1
        # for j in range(len(snake)):
        #     print(j,snake[j].x,snake[j].y)
       
        # food_object=Food()
        
        # food_x = int(DIMENSION*random()/20)*20
        # food_y = int(DIMENSION*random()/20)*20
        # point=0
        # if new_l == l+20:

        #     point+=10
            # print("current score :",point)

    # draw the snake
    for i in range(len(snake)):
        # if i==0:# the head
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(snake[i].x,snake[i].y,20,20))
    # else: # the body parts
        # pygame.draw.rect(screen,(0,0,255),pygame.Rect(snake[0].x,snake[0].y,20,20))
    # record the point

    # font=pygame.font.SysFont("Arial",36)
    # txtsurf=font.render(str(y),True,(255,255,255))
    # txtsurf=font.render(str(y).encode("utf-8").decode("utf-8"),True,(255,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(200, 200))
    # for s in range(len(snake)):
    #     print(list(snake[s]))
    pygame.display.update()

pygame.quit()
