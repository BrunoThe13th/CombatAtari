import turtle
import random

file = open('labirinto.txt', 'r')
wall = file.readlines()


# Funçao que gera as paredes
def generate_walls(x, y):
    posy_block = 200
    for lines in range(x):
        posx_block = -353
        for columns in range(y):
            block = turtle.Turtle("square")
            block.speed(0)
            block.color("")
            block.shapesize(0.5, 0.5)
            block.penup()
            block.goto(posx_block, posy_block)
            posx_block += 10
        posy_block -= 10

file.close()
