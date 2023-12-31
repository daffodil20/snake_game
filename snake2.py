import pygame
import time
from random import random

DIMENSION = 400
pygame.init()
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
running = True

food_timer = time.time()
grid_timer = time.time()
snake_timer = time.time()

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
    
    else:
        draw_food = pygame.Rect(foods[current_food].x,foods[current_food].y,20,20)
        pygame.draw.rect(screen,(0,255,255),draw_food)
    # snake automatic moves

    if delay_counter == len(direction):
        delay_counter = 1

# the direction of latter is the same as its front one

    if time.time()-snake_timer > 0.5:
        if len(direction) > 1 and delay_counter < len(direction):
            if direction[len(direction)-delay_counter] != direction[len(direction)-delay_counter-1]:
                direction[len(direction)-delay_counter] = direction[len(direction)-delay_counter-1]
                # temp_direction = direction[delay_counter-1]
                # direction[delay_counter] = temp_direction
                print(direction[delay_counter])
                # direction[len(direction)-delay_counter] = direction[len(direction)-delay_counter-1]
                delay_counter += 1
                
            # print(direction[0],direction[1])

    if time.time()-grid_timer > 0.5:
        for i in range(len(snake)):
        # judge the direction of the moving parts
            if direction[i] == 0:
                snake[i].y -= 20
                # snake[i].y = boundary(snake[i].y)
            if direction[i] == 1:
                snake[i].x += 20
                # snake[i].x = boundary(snake[i].x)
            if direction[i] == 2:
                snake[i].y += 20
                # snake[i].y = boundary(snake[i].y)
            if direction[i] == 3:
                snake[i].x -= 20
        grid_timer = time.time()
    
    #events triggered by keyboard 
    for event in pygame.event.get():
        # print(direction)
        if event.type ==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            
            # print(snake)
            # print(direction)
            if event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                key_direct = 2
                if key_direct - direction[0] != 2 and key_direct - direction[0] != -2:
                    dir=2
                    direction[0] = dir
                # snake[0].y += 20
            if event.key == pygame.K_UP or event.key == pygame.K_KP8:
                key_direct = 0
                if key_direct - direction[0] != 2 and key_direct - direction[0] != -2:
                    dir=0
                    direction[0] = dir
                # snake[0].y -= 20
            if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                key_direct = 3
                if key_direct - direction[0] != 2 and key_direct - direction[0] != -2:
                    dir=3
                    direction[0] = dir
                # snake[0].x -= 20
            if event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                key_direct = 1
                if key_direct - direction[0] != 2 and key_direct - direction[0] != -2:
                    dir=1
                    direction[0] = dir
                # snake[0].x += 20
            # snake_timer = time.time()
            # grid_timer = time.time()
            for i in range(len(snake)):
        # judge the direction of the moving parts
                if direction[i] == 0:
                    snake[i].y -= 20
                    # snake[i].y = boundary(snake[i].y)
                if direction[i] == 1:
                    snake[i].x += 20
                    # snake[i].x = boundary(snake[i].x)
                if direction[i] == 2:
                    snake[i].y += 20
                    # snake[i].y = boundary(snake[i].y)
                if direction[i] == 3:
                    snake[i].x -= 20
                
                # snake[0].x = boundary(snake[0].x)  

            #     #eat food
    if foods[current_food].x == snake[0].x and foods[current_food].y == snake[0].y:
        if direction[len(direction)-1] == 0:
            tail_x = snake[len(snake)-1].x
            tail_y = snake[len(snake)-1].y+20
        if direction[len(direction)-1] == 1:
            tail_x = snake[len(snake)-1].x-20 
            tail_y = snake[len(snake)-1].y
        if direction[len(direction)-1] == 2:
            tail_x = snake[len(snake)-1].x
            tail_y = snake[len(snake)-1].y-20
        if direction[len(direction)-1] == 3:
            tail_x = snake[len(snake)-1].x+20
            tail_y = snake[len(snake)-1].y
        # print(snake[len(snake)-1].x,snake[len(snake)-1].y)
        # print(tail_x,tail_y)
        # print(direction[len(direction)-1])
        # snake_object = unit(tail_x,tail_y)
        # snake.append([tail_x, tail_y])
        foods[current_food].x=tail_x
        foods[current_food].y=tail_y
        # snake_object = Unit(tail_x,tail_y)
        snake.append(foods[current_food])
        foods.pop(current_food)
        direction.append(direction[len(direction)-1])
        # delay_counter = 1

    if snake[0].x == DIMENSION or snake[0].x == 0 or snake[0].y == DIMENSION or snake[0].y == 0:
        running = False
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
