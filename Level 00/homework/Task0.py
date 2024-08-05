# Draw the house.

from turtle import *



bgcolor("lightblue")
width(7)
color("blue")


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
pendown()

color("yellow")
begin_fill()
left(300)
forward(50)

left(90)
forward(30)

left(90)
forward(50)

left(90)
forward(30)

end_fill()

penup()
goto(30, 170)

pendown()
color("yellow")
begin_fill()
right(90)
forward(50)

right(90)
forward(30)

right(90)
forward(50)

right(90)
forward(30)
end_fill()
exitonclick()