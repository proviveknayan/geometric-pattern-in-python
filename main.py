from turtle import *
import random

screen = Screen() # create screen
screen.screensize(400, 400, "#000000") # set screen

pen = Pen() # create pen
pen.speed(75) # set pen speed
size = 20

for i in range(150):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcolor = (r,g,b) # set color information
    colormode(255) # use color
    pen.color(randcolor) # set pen color
    pen.circle(size, steps=4) # create a square
    pen.right(55) #turn the pen 55 degrees
    size = size +3 #increase the size of the square
