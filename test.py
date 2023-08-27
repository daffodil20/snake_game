from random import random
DIMENSION = 10
class Unit:
    x=0
    y=0
    def __init__(self,food_x,food_y) -> None:
        self.x=food_x
        self.y=food_y

foods=[]
for i in range(100):
    food_x= int(DIMENSION*random()/20)*20
    food_y= int(DIMENSION*random()/20)*20
    food_object = Unit(food_x,food_y)
    foods.append(food_object)
print(list(food_object))