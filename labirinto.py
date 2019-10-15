import turtle
import random


# Funçao que gera as paredes
def generate_walls(x, y):
    file = open('labirinto.txt', 'r')
    wall = file.readlines()
    posy_block = 200
    for lines in range(x):
        wall1 = wall[lines].strip().split(",")
        posx_block = -353
        for columns in range(y):
            if (wall1[columns] == '1'):
                block = turtle.Turtle("square")
                block.speed(0)
                block.color("white")
                block.shapesize(0.5, 0.5)
                block.penup()
                block.goto(posx_block, posy_block)
            posx_block += 10
        posy_block -= 10
    file.close()
