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
    color(colors[i])
    snowflake_side(length, sides)
    right(360 / sides)
    
speed(0)
create_snowflake(4,200)

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

speed(0)
left(90)
tree(90, 6, 20)
left(180)
tree(90, 6, 20)
left(90)
tree(90, 6, 20)
left(180)
tree(90, 6, 20)
left(90)
tree(60, 6, 20)
left(180)
tree(60, 6, 20)
left(90)
tree(60, 6, 20)
left(180)
tree(60, 6, 20)
  
mainloop()


