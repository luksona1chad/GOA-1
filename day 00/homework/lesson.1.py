from turtle import *


#step 1: draw a house
speed(7)
shape ("arrow")
#we want to paint a house
width(1)
begin_fill()
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(180)
forward(200)
end_fill()







#roof


color("red")
begin_fill()
right(30)
forward(200)
right(120)
forward(200)
end_fill()

#door

color("purple")
right(30)
forward(200)
right(90)
forward(70)
right(90)
color("yellow")
begin_fill()
forward(120)
left(90)
forward(50)
left(90)
forward(120)
end_fill()

#window 1


penup()
goto(150,160)
color("purple")
right(90)
forward(10)
color("blue")
begin_fill()
pendown()
right(90)
forward(35)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#window 2

left(90)
penup()
forward(135)
right(180)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
end_fill()





exitonclick()

