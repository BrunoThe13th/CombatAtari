import turtle
import time
from labirinto import generate_walls
from math import sqrt

angulo_1 = 0
angulo_2 = 180
# intervalo de atualização do projetil
tempo = 0.015
placar1 = 0
placar2 = 0

# Parametros fonte do placar
fonte = ("Comic Sans", 25, "normal")

# Criando Tela
screen = turtle.Screen()
screen.title("Combat_atari")
screen.bgcolor("green")
screen.setup(720, 480)
screen.tracer(0)

obstaculos = []
# Gerando labirinto
# Armazena as coordenadas dos obstáculos criados na lista
obstaculos = generate_walls(44, 71)

# Criando jogador 1
player_1 = turtle.Turtle("turtle")
player_1.speed(0)
player_1.turtlesize(2.0, 2.0)
player_1.color("blue")
player_1.penup()
player_1.setx(-330)

# Criando jogador 2
player_2 = turtle.Turtle("turtle")
player_2.speed(0)
player_2.turtlesize(2.0, 2.0)
player_2.left(180)
player_2.color("red")
player_2.penup()
player_2.setx(330)

# Criando placar 1
placar_1 = turtle.Turtle("turtle")
placar_1.speed(0)
placar_1.turtlesize(1.0, 1.0)
placar_1.left(180)
placar_1.color("black")
placar_1.penup()
placar_1.setx(-290)
placar_1.sety(204)
placar_1.ht()
placar_1.write(placar1, False, "center", fonte)

# Criando placar 2
placar_2 = turtle.Turtle("turtle")
placar_2.speed(0)
placar_2.turtlesize(1.0, 1.0)
placar_2.left(180)
placar_2.color("black")
placar_2.penup()
placar_2.setx(290)
placar_2.sety(204)
placar_2.ht()
placar_2.write(placar2, False, "center", fonte)


# Rotação dos jogadores para a direita
def player1_movement_right():
    player_1.right(30)
    global angulo_1
    angulo_1 -= 30
    if angulo_1 == 360:
        angulo_1 = 0


def player2_movement_right():
    player_2.right(30)
    global angulo_2
    angulo_2 -= 30
    if angulo_2 == 360:
        angulo_2 = 0


# Rotação dos jogadores para a esquerda
def player1_movement_left():
    player_1.left(30)
    global angulo_1
    angulo_1 += 30
    if angulo_1 == 360:
        angulo_1 = 0


def player2_movement_left():
    player_2.left(30)
    global angulo_2
    angulo_2 += 30
    if angulo_2 == 360:
        angulo_2 = 0

# Movimentação dos jogadores para a frente


def player1_movement_forward():
    pos1_xy = player_1.pos()
    pos2_xy = player_2.pos()
    if ((sqrt((pos1_xy[0]-pos2_xy[0])**2) +
         ((pos1_xy[1]-pos2_xy[1])**2)) > 40):
        player_1.forward(10)


def player2_movement_forward():
    pos1_xy = player_1.pos()
    pos2_xy = player_2.pos()
    if ((sqrt((pos2_xy[0]-pos1_xy[0])**2) +
         ((pos2_xy[1]-pos1_xy[1])**2)) > 40):
        player_2.forward(10)


def tiro_p1():
    global placar1

    tiro1 = turtle.Turtle()
    tiro1.up()
    tiro1.shape('circle')
    tiro1.turtlesize(0.5, 0.5)
    tiro1.setpos(player_1.pos())
    tiro1.left(angulo_1)

    # Posicao de Tiro1
    pos_tiro1_xy = player_1.pos()
    # Posicao do player 2
    pos_p2_xy = player_2.pos()
    print('t1_pos', tiro1.pos())
    print('xcor', round(tiro1.xcor(), 0))
    print('ycor', round(tiro1.ycor(), 0))
    print('distancia', (sqrt(
        (pos_tiro1_xy[0]-pos_p2_xy[0])**2) +
        ((pos_tiro1_xy[1]-pos_p2_xy[1])**2)))
    print('angulo', angulo_1)
    print('-----')

    while ((round(tiro1.xcor(), 0) in range(-350, 350)) and (round(tiro1.ycor(), 0) in range(-220, 220))) and ((sqrt((pos_tiro1_xy[0]-pos_p2_xy[0])**2) + ((pos_tiro1_xy[1]-pos_p2_xy[1])**2)) > 50):
        screen.update()
        screen.update()
        tiro1.forward(10)
        time.sleep(tempo)

        # Posicao de Tiro1
        pos_tiro1_xy = tiro1.pos()
        # Posicao do player 2
        pos_p2_xy = player_2.pos()

    # Se tiro atingir P2
    if ((sqrt((pos_tiro1_xy[0]-pos_p2_xy[0])**2) +
         ((pos_tiro1_xy[1]-pos_p2_xy[1])**2)) <= 50):
        placar1 += 1
        placar_1.clear()
        placar_1.write(placar1, False, "center", fonte)

    # tiro1.ht()


def tiro_p2():
    global placar2

    tiro2 = turtle.Turtle()
    tiro2.up()
    tiro2.shape('circle')
    tiro2.turtlesize(0.5, 0.5)
    tiro2.setpos(player_2.pos())
    tiro2.left(angulo_2)

    # Posicao de Tiro2
    pos_tiro2_xy = player_2.pos()
    # Posicao do player 1
    pos_p1_xy = player_1.pos()

    while ((round(tiro2.xcor(), 0) in range(-350, 350)) and (round(tiro2.ycor(), 0) in range(-220, 220))) and ((sqrt((pos_tiro2_xy[0]-pos_p1_xy[0])**2) + ((pos_tiro2_xy[1]-pos_p1_xy[1])**2)) > 50):
        screen.update()
        screen.update()
        tiro2.forward(10)
        time.sleep(tempo)

        # Posicao de Tiro2
        pos_tiro2_xy = tiro2.pos()
        # Posicao do player 1
        pos_p1_xy = player_1.pos()

    # Se tiro atingir P1
    if ((sqrt((pos_tiro2_xy[0]-pos_p1_xy[0])**2) +
         ((pos_tiro2_xy[1]-pos_p1_xy[1])**2)) <= 50):
        placar2 += 1
        placar_2.clear()
        placar_2.write(placar2, False, "center", fonte)

    # tiro2.ht()


screen.onkeypress(player1_movement_forward, 'w')
screen.onkeypress(player1_movement_left, 'a')
screen.onkeypress(player1_movement_right, 'd')
screen.onkeypress(player2_movement_left, 'Left')
screen.onkeypress(player2_movement_right, 'Right')
screen.onkeypress(player2_movement_forward, 'Up')
screen.onkeypress(tiro_p1, "space")
screen.onkeypress(tiro_p2, '0')
screen.listen()


while True:
    screen.update()
    screen.update()

    # Limitações da tela no eixo X
    if player_1.xcor() > 335:
        player_1.setx(335)
    if player_1.xcor() < -335:
        player_1.setx(-335)
    if player_2.xcor() > 335:
        player_2.setx(335)
    if player_2.xcor() < -335:
        player_2.setx(-335)

    # Limitações da tela no eixo Y
    if player_1.ycor() > 220:
        player_1.sety(220)
    if player_1.ycor() < -220:
        player_1.sety(-220)
    if player_2.ycor() > 220:
        player_2.sety(220)
    if player_2.ycor() < -220:
        player_2.sety(-220)

screen.exitonclick()
