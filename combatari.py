import turtle

screen = turtle.Screen()
screen.title("Combat_atari")
screen.bgcolor("green")
screen.setup(720,720)
screen.tracer(0)

player_1 = turtle.Turtle("turtle")
player_1.speed(0)
player_1.turtlesize(1.5,1.5)
player_1.color("blue")
player_1.penup()
player_1.setx(330)

player_2 = turtle.Turtle("turtle")
player_2.speed(0)
player_2.turtlesize(1.5,1.5)
player_2.color("red")
player_2.penup()
player_2.setx(-330)

def player1_movement_right():
    player_1.right(30)
def player2_movement_right():
    player_2.right(30)
def player1_movement_left():
    player_1.left(30)
def player2_movement_left():
    player_2.left(30)
def player1_movement_forward():
    player_1.forward(15)
def player2_movement_forward():
    player_2.forward(15)

screen.onkeypress(player1_movement_left,'a')
screen.onkeypress(player1_movement_right,'d')
screen.onkeypress(player2_movement_left,'Left')
screen.onkeypress(player2_movement_right,'Right')
screen.onkeypress(player1_movement_forward,'w')
screen.onkeypress(player2_movement_forward,'Up')
screen.listen()



while True:
    screen.update()
    screen.update()