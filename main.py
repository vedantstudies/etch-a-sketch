import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()

def forwards():
    tim.forward(distance=10)

def backwards():
    tim.backward(distance=10)

def turn():
    tim.left(angle=90)

def clockwise():
    tim.circle(radius=-100, extent=10)

def counter_clockwise():
    tim.circle(radius=100, extent=10)

def clear_drawing():
    tim.clear()

    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="t", fun=turn)
screen.onkey(key="Up", fun=forwards)
screen.onkey(key="Down", fun=backwards)
screen.onkey(key="Right", fun=clockwise)
screen.onkey(key="Left", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
