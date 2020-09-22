#PythonMiniProject
#bybinam karki
#learnin to code
#ponggame
#turtle module

#importing turtle

import turtle
import winsound

#Creating game screen
wingame = turtle.Screen()
wingame.title("Pong Game By Binam")
wingame.bgcolor("teal")
wingame.setup(height=600, width=800)
wingame.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx= 0.5
ball.dy= -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player Red: 0     Player Blue: 0", align="center", font=("Courier", 24, "normal"))

#Function

# function for moving paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# function for moving paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# function for moving paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# function for moving paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard Binding

wingame.listen()
wingame.onkeypress(paddle_a_up, "w")
wingame.onkeypress(paddle_a_down, "s")
wingame.onkeypress(paddle_b_up, "Up")
wingame.onkeypress(paddle_b_down, "Down")



#Main Game Loop

while True:
    wingame.update()


    #moving the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Brder Checking

    #Height is 600, So half height is 300
    #ball is of 20px, so we will work on 290px

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #so this code is for importing sound which is different for Win,mac and linux

        #for mac
        #import os
        #os.system("afplay bounce.wav&")

        #for linux
        #import os
        #os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #width is 800, So half height is 4
    #ball is of 20px, so we will work on 390px

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player Red: {}     Player Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player Red: {}     Player Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Paddle 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # turtle_module

   
    
