#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:27:43 2020

@author: mackenziebraun
"""

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)
style=('courier', 40, 'bold')
color('black')
up()
speed(0)
goto(110,-110)
write('pajAMAZ ON!', font=style, align='left')
color('orange')

goto(190,-115)
pensize(5)
down()
right(90)
circle(35,180)
right(135)
fd(8)
back(5)
right(135)
fd(8)
up()



color ("DarkOrange")
goto(70,180)
right(180)
down()
begin_fill()
for _ in range(1):
    back(175)
    left(90)
    fd(25)
    right(90)
    fd(175)
    right(90)
    fd(25)
end_fill()

right(90)
fd(10)
right(90)
fd(25)
color('orange')

begin_fill()
for _ in range (1):
    fd(15)
    left(45)
    fd(60)
    fd(40)
    left(45)
    fd(50)
    fd(30)
    left(60)
    fd(100)
    left(30)
    fd(50)
    left(90)
    fd(20)
    right(180)
    circle(30)
    right(180)
    fd(20)
    left(90)
    fd(50)
end_fill()
right(90)
color([255,255,255])
pensize(10)
up()
fd(5)
down()
fd(160)
    
    

    
    
    
 
    



