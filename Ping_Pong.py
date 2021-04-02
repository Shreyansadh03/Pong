#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:28:37 2021

@author: shreyan
"""

import turtle
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
xres = 1024
yres = 720
wn.setup(width = xres, height = yres)
wn.tracer(0)

#padde 1

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.penup()
paddle1.color("green")
paddle1.goto(-(xres/2 - 50),0)
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)

#paddle 2

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.penup()
paddle2.color("red")
paddle2.goto(xres/2 - 50,0)
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)

#Ball

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.penup()
ball.color("black")
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

# Score Board

board = turtle.Turtle()
board.speed(0)
board.penup()
board.color("black")
board.hideturtle()
board.goto(0,yres/2 - 50)
board.write("Player A = 0 | Player B = 0", align = "center", font = ("Consolas",16,"normal"))

score1 = 0
score2 = 0

#Paddle1 Movement

def paddle1_up():
    y = paddle1.ycor()
    y += 10
    y = paddle1.sety(y)
    if paddle1.ycor() >= yres/2 - 60:
        y = paddle1.sety(yres/2 - 60)

def paddle1_down():
    y = paddle1.ycor()
    y -= 10
    y = paddle1.sety(y)
    if paddle1.ycor() <= -(yres/2 - 60):
        y = paddle1.sety(-(yres/2 - 60))
    
#Paddle2 Movement

def paddle2_up():
    y = paddle2.ycor()
    y += 10
    y = paddle2.sety(y)
    if paddle2.ycor() >= yres/2 - 60:
        y = paddle2.sety(yres/2 - 60)

def paddle2_down():
    y = paddle2.ycor()
    y -= 10
    y = paddle2.sety(y)
    if paddle2.ycor() <= -(yres/2 - 60):
        y = paddle2.sety(-(yres/2 - 60))

#Controls

wn.listen()
wn.onkeypress(paddle1_up,'w')
wn.onkeypress(paddle1_down,'s')
wn.onkeypress(paddle2_up,'o')
wn.onkeypress(paddle2_down,'l')


while True:
    wn.update()
    
    # Ball Movement
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Boundry Check
    
    if ball.ycor() > yres/2 - 20:
        ball.sety(yres/2 - 20)
        ball.dy *= -1
        
    if ball.ycor() < -(yres/2 - 20):
        ball.sety(-(yres/2 - 20))
        ball.dy *= -1
        
    if ball.xcor() > xres/2 - 10:
        ball.goto(0,0)
        # if random.random() > 0.5:
        #     ball.dx *= -1 
        # else:
        #     ball.dx *= 1
        ball.dx *= random.uniform(0.9,1)
        score1 += 1
        board.clear()
        board.write("Player A = {} | Player B = {}".format(score1,score2), align = "center", font = ("Consolas",16,"normal"))
        
    if ball.xcor() < -(xres/2 - 10):
        ball.goto(0,0)
        # if random.random() > 0.5:
        #     ball.dx *= -1 
        # else:
        #     ball.dx *= 1
        ball.dx *= random.uniform(0.9,1)
        score2 += 1
        board.clear()
        board.write("Player A = {} | Player B = {}".format(score1,score2), align = "center", font = ("Consolas",16,"normal"))    

    
    # Ball and paddle collision
    
    if ball.xcor() > xres/2 - 70 and ball.xcor() < xres/2 - 40 and ball.ycor() < paddle2.ycor() + 60 and ball.ycor() > paddle2.ycor() - 60:
        ball.setx(xres/2 - 70)
        ball.dx *= -1
    
    if ball.xcor() < -(xres/2 - 70) and ball.xcor() > -(xres/2 - 40) and ball.ycor() < paddle1.ycor() + 60 and ball.ycor() > paddle1.ycor() - 60:
        ball.setx(-(xres/2 - 70))
        ball.dx *= -1
