from turtle import *

#2D graphics odule in python --> for very simple visualizing 

#speed(0) --> very fast
#shape("turtle")
#forward(100)
#left(45)
#forward(100)
#right(45)
#forward(10)
#backward(200)

def snowflake_side(length, levels):
  if levels == 0:
      forward(length)
      return

  length /= 3.0
  snowflake_side(length, levels - 1)
  left(60)
  snowflake_side(length, levels - 1)
  right(120)
  snowflake_side(length, levels - 1)
  left(60)
  snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
  colors = ["green", "blue", "yellow", "orange"]
  for i in range(sides):
    #color(colors[i])
    snowflake_side(length, sides)
    right(360 / sides)
    
#speed(0)
#create_snowflake(3,100)

def tree(size, levels, angle):
  if levels == 0:
    color("green")
    dot(size)
    color("black")
    return
  forward(size)
  right(angle)  

  tree(size * 0.8, levels -1, angle)
  
  left(angle * 2)
  
  tree(size * 0.8, levels -1, angle)

  right(angle)
  backward(size)

def snowflake_circle(count, degree, side, size):
  speed(0)
  for i in range(count):
    size = size + (i * 10)
    for i in range(3):
      left(degree + 30)
      create_snowflake(side, size)

#snowflake_circle(15, 90, 3, 150)

def recursion_threes(count, starting_degree, size, levels, angle):
  speed(0)
  for i in range(count):
    size -= 10
    levels -= 1
    for i in range(4):
      left(starting_degree)
      tree(size, levels, angle)
      if starting_degree == 180:
        starting_degree = 90

#recursion_threes(5, 90, 90, 7, 20)  

def shell(level, a, angle, growth):
  speed(0)
  if level == 0:
    return
  forward(a)
  right(angle)
  forward(a)
  right(angle)
  forward(a + growth)
  right(angle)
  forward(a + growth)
  right(angle)
  shell(level - 1, a + (2 * growth), angle, growth)

for i in range(10):
  shell(20, 2, 90, 2)
  right(45)


"""
speed(0)
tree(150, 8, 300)
right(180)
tree(150, 8, 310)
"""


"""
speed(0)
left(90)
tree(90, 6, 20)
create_snowflake(3,100)
left(180)
tree(90, 6, 20)
create_snowflake(3,100)
left(90)
tree(90, 6, 20)
create_snowflake(3,100)
left(180)
tree(90, 6, 20)
create_snowflake(3,100)
left(90)
tree(60, 6, 20)
create_snowflake(3,100)
left(180)
tree(60, 6, 20)
create_snowflake(3,100)
left(90)
tree(60, 6, 20)
create_snowflake(3,100)
left(180)
tree(60, 6, 20)
create_snowflake(3,100)
tree(30, 6, 20)
create_snowflake(3,100)
left(180)
tree(30, 6, 20)
create_snowflake(3,100)
left(90)
tree(30, 6, 20)
create_snowflake(3,100)
left(180)
tree(30, 6, 20)
create_snowflake(3,100)
"""
mainloop()


