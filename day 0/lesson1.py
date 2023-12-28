from turtle import *


# we want to paint a house

# step 1: draw a square

speed(30)
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
# end of square

# drawing of door

forward(70)
color("black")
begin_fill()
left(90)
forward(95)   # height of the door
right(90)
forward(60)
right(90)
forward(95)
end_fill()

# begging of roof

penup()
goto (200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# drawing the windows

penup()
goto(200, 140)
left(300)
forward(65)
pendown()
color("brown")
begin_fill()
left(270)
forward(30)
left(270)
forward(30)
left(270)
forward(30)
left(270)
forward(30)
end_fill()

penup()
forward(100)
left(270)
pendown()
color("brown")
begin_fill()
forward(30)
left(270)
forward(30)
left(270)
forward(30)
left(270)
forward(30)
end_fill()




exitonclick()