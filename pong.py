# Basic pong game 

import turtle as tl
import random
import time
import os

#Variables

global scoreLeft
global scoreRight
scoreLeft = 0
scoreRight = 0
activeThing = True
window = tl.Screen()
ball = tl.Turtle()
scoreBoard = tl.Turtle()
leftPaddle = tl.Turtle()
rightPaddle = tl.Turtle()
winMessage = tl.Turtle()

#Window game

window.title("Pong")
window.bgcolor("Black")
window.setup(height = 600, width = 800)
window.tracer(0)

#Scoreboard

scoreBoard.speed(0)
scoreBoard.color("white")
scoreBoard.goto(-50, 200)
scoreBoard.penup()
scoreBoard.hideturtle()

#Win message

winMessage.speed(0)
winMessage.color("white")
winMessage.goto(-200, 0)
winMessage.penup()
winMessage.hideturtle()


#Paddle left

leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid = 5, stretch_len=1)
leftPaddle.penup() # No line drawn
leftPaddle.goto(-350, 0)

#Paddle right

rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid = 5, stretch_len=1)
rightPaddle.penup() # No line drawn
rightPaddle.goto(350, 0)

#Ball

def createBall():

    rand_num = random.choice([1, -1])
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup() # No line drawn
    ball.goto(0, 0)
    ball.dx = 5*rand_num
    ball.dy = 6*rand_num

createBall()

#Movement

def leftUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)
def rightUp():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)
def leftDown():
    y = leftPaddle.ycor()
    y += -20
    leftPaddle.sety(y)
def rightDown():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)

#Collisions

def checkCollisions():

    #Limits

    if (abs(window.window_height()/2 - ball.ycor()) <= 20):
        ball.dy *= -1
    if (abs(-window.window_height()/2 - ball.ycor()) <= 15):
        ball.dy *= -1


    #Paddle

    if (abs(leftPaddle.xcor() - ball.xcor()) <= 20 and abs(leftPaddle.ycor() - ball.ycor()) <= 40):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if (abs(rightPaddle.xcor() - ball.xcor()) <= 20 and abs(rightPaddle.ycor() - ball.ycor()) <= 40):
        os.system("afplay bounce.wav&")
        ball.dx *= -1

def checkPoints():

    global scoreLeft
    global scoreRight

    #If scores create another ball in the center

    if (ball.xcor() == window.window_width()/2 - 20):
        ball.hideturtle()
        window.ontimer(createBall, 3000)
        ball.showturtle()
        scoreLeft += 1
    if (ball.xcor() == -window.window_width()/2 + 20):
        ball.hideturtle()
        window.ontimer(createBall, 3000)
        ball.showturtle()
        scoreRight += 1

def actuaScore():
    scoreBoard.clear()
    scoreBoard.write(str(scoreLeft) + " - " + str(scoreRight), font=("Pixel", 50, "normal"))

#Keyboard

window.listen()
window.onkey(leftUp, "w")
window.onkey(leftDown, "s")
window.onkey(rightUp, "Up")
window.onkey(rightDown, "Down")

#Main loop

while(activeThing):

    winMessage.clear()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    checkCollisions()

    checkPoints()

    actuaScore()

    window.update()

    #Check scores

    if (scoreLeft == 5):

        winMessage.write("LEFT WINS!!!! ", font=("Pixel", 50, "normal"))
        time.sleep(2)
        activeThing = False

    elif (scoreRight == 5):

        winMessage.write("RIGHT WINS!!!! ", font=("Pixel", 50, "normal"))
        time.sleep(2)
        activeThing = False

tl.bye()



