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
#good on you for using the write function. I didn't know it till now!. - Owen
write('pajAMAZ ON!', font=style, align='left')
color('orange')

#this could need a comment. I don't know what this is, or what it does. - Owen
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


#same here. This section could need comments so I know what it is and what you're doing. - Owen
color ("DarkOrange")
goto(70,180)
right(180)
down()
begin_fill()
for _ in range(1):
    #certain parts of this block can be executed with a for loop. - Owen
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

#again, use more comments so I know what this is. I'm assuming that each block of code is for a different part of the drawing, but that's slightly unclear. - Owen 
begin_fill()
#if this is done only once (range(1)) is it really necessary to have this loop in the first place? - Owen
for _ in range (1): 
    #also good on you for abbreviating foward to fd. Saves a ton of time. Well done. - Owen
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
#it might be easier here to just say white. Why enter all those numbers when you can just type out the words??
color([255,255,255])
pensize(10)
up()
fd(5)
down()
fd(160)
    
    

    
    
    
 
    



