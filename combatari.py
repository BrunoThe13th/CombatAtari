import turtle
from labirinto import generate_walls

# Criando Tela
screen = turtle.Screen()
screen.title("Combat_atari")
screen.bgcolor("green")
screen.setup(720, 480)
screen.tracer(0)

# Gerando labirinto
generate_walls(44, 71)

# Criando jogador 1
player_1 = turtle.Turtle("turtle")
player_1.speed(0)
player_1.turtlesize(1.5, 1.5)
player_1.color("blue")
player_1.penup()
player_1.setx(-330)

# Criando jogador 2
player_2 = turtle.Turtle("turtle")
player_2.speed(0)
player_2.turtlesize(1.5, 1.5)
player_2.left(180)
player_2.color("red")
player_2.penup()
player_2.setx(330)


# Rotação dos jogadores para a direita
def player1_movement_right():
    player_1.right(30)


def player2_movement_right():
    player_2.right(30)


# Rotação dos jogadores para a esquerda
def player1_movement_left():
    player_1.left(30)


def player2_movement_left():
    player_2.left(30)


# Movimentação dos jogadores para a frente
def player1_movement_forward():
    player_1.forward(15)


def player2_movement_forward():
    player_2.forward(15)


screen.onkeypress(player1_movement_left, 'a')
screen.onkeypress(player1_movement_right, 'd')
screen.onkeypress(player2_movement_left, 'Left')
screen.onkeypress(player2_movement_right, 'Right')
screen.onkeypress(player1_movement_forward, 'w')
screen.onkeypress(player2_movement_forward, 'Up')
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
