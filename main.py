# Authour: Ajay saini
# Date: 6/13/2024
# Purpose: To create a city skyline using python (Turtle)

import turtle, random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("Dark blue")


def crescent():
  crescent = turtle.Turtle()
  crescent.speed(0)
  crescent.goto(-175, 120)
  crescent.begin_fill()
  crescent.color("yellow")
  crescent.circle(50)
  crescent.end_fill()
  # Second circle to cover and create crescent shape
  crescent.speed(0)
  crescent.goto(-160, 120)
  crescent.begin_fill()
  crescent.color("Dark blue")
  crescent.circle(50)
  crescent.end_fill()


def stars():
  turtle.fillcolor("white")
  for i in range(30):  #number of stars
    x_position = random.randint(-300, 400)
    y_position = random.randint(50, 200)
    turtle.penup()
    turtle.goto(x_position, y_position)  #area where i want the stars to be
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.speed(0)


def skyscrappers():
  turtle.penup()
  turtle.goto(-250,-250)
  turtle.pendown()
  turtle.fillcolor("grey")
  turtle.begin_fill()
  turtle.forward(45)
  turtle.left(90)
  turtle.forward(120)
  turtle.right(90)
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(90)
  turtle.right(90)
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(110)
  turtle.right(90)
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(80)
  turtle.left(90)
  turtle.forward(130)
  turtle.right(90)
  turtle.forward(75)
  turtle.right(90)
  turtle.forward(90)
  turtle.left(90)
  turtle.forward(80)
  turtle.left(90)
  turtle.forward(80)
  turtle.right(90)
  turtle.forward(90)
  turtle.right(90)
  turtle.forward(150)
  turtle.left(90)
  turtle.forward(70)
  turtle.right(90)
  turtle.forward(70)
  turtle.left(90)
  turtle.forward(70)
  turtle.right(90)
  turtle.forward(150)
  turtle.end_fill()

def windows_on_skyscrappers():
    turtle.speed(0)
    turtle.fillcolor("white")
    turtle.penup()
    turtle.goto(-140,-80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)

  #first window
    for i in range(4):
      turtle.forward(10)
      turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-40,60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
  #second window
    for i in range(4):
      turtle.forward(10)
      turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-40,-60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
  #third window
    for i in range(4):
      turtle.forward(10)
      turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(160,00)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
  #fourth window
    for i in range(4):
      turtle.forward(10)
      turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-40,60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)


stars()
skyscrappers()
windows_on_skyscrappers()
crescent()

screen.mainloop()
