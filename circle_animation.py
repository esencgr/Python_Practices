# -*- coding: utf-8 -*-
import random
import turtle
import tkinter as tk

tr = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor( "grey" )

def circles( tr ):
    x = random.sample( range( -180, 180 ), 20 )
    y = random.sample( range( -180, 180 ), 20 )
    for i in range( 0, 4 ):
        tr.penup() 
        tr.setposition( x[i], y[i] )
        tr.pendown()
        tr.circle( random.randint( 5, 75 ) )

def line( t ):
    for x in range( 0, 50, 2 ):
        t.forward( x )
        t.left( 90 )

line( tr )
sc.clear()

sc.bgcolor( "gray" )
circles( tr )

tk.mainloop()
turtle.getscreen()._root.mainloop()
turtle.bye()

