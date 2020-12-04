## Estudar metapragramação python


#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

import turtle

turtle.setup(800, 600)
board = turtle.Turtle()

board.penup()
board.setpos(0, 0)
board.pendown()
board.circle(100)

turtle.done()