import turtle
from turtle import *

turtle.setup(480, 480)
speed(0)
hideturtle()
pencolor("#000")
pensize(2)
pu()
goto(120, 90)
fillcolor("#FDF2E5")
begin_fill()
pd()
goto(0, 70)
goto(-100, 100)
goto(-90, 50)
goto(-100, -100)
pencolor("#fdf2e5")
goto(-5, -205)
goto(45, -205)
goto(100, -100)
pencolor("#000")
goto(120, 90)
end_fill()
pu()
fillcolor("#D3FDFF")
goto(-15, -130)
pd()
begin_fill()
goto(15, -140)
goto(45, -130)
pencolor("#fdf2e5")
goto(45, -205)
goto(-5, -205)
goto(-20, -150)
goto(-15, -130)
end_fill()
pu()
pencolor("#000")
goto(50, 100)
pd()
fillcolor("#4D3938")
begin_fill()
left(150)
circle(100, 90)
circle(200, extent=10)
circle(120, 10)
circle(120, 10)
for i in range(1, 2):
    left(-10)
    circle(200, 10)
left(-25)
circle(150, 55)
right(25)
circle(150, -25)
left(15)
circle(110, 50)
circle(20, 50)
right(75)
circle(100, -20)
left(25)
goto(-25, -210)
goto(-25, -180)
goto(-5, -210)
right(5)
circle(150, -35)
left(100)
circle(70, -70)
left(160)
circle(-300, 17)
right(70)
circle(100, 60)
left(45)
circle(-250, -5)
circle(-45, -60)
right(60)
circle(250, -25)
right(37)
circle(100, -35)
left(100)
circle(150, -33)
goto(60, -170)
circle(-35, -90)
right(30)
circle(-35, 45)
right(155)
circle(45, 60)
goto(119, -170)
left(130)
circle(50, -50)
right(20)
circle(90, 40)
goto(141, -20)
circle(156, 58)
end_fill()
pu()
goto(0, -70)
pd()
pencolor("#A93535")
fillcolor("#a93535")
begin_fill()
goto(30, -72)
right(50)
circle(15, -180)
end_fill()
fillcolor("#E07467")
begin_fill()
pu()
circle(15, 20)
pd()
right(90)
circle(20, -75)
right(80)
circle(15, -130)
end_fill()
pu()
pencolor("#fff")
goto(-15, -50)
fillcolor("#fff")
begin_fill()
pd()
goto(-50, -47)
circle(20, -240)
end_fill()
fillcolor("#824652")
pencolor("#824652")
begin_fill()
circle(20, 110)
left(25)
circle(20, 110)
end_fill()
pu()
goto(-30, -38)
pencolor("#fff")
fillcolor("#fff")
begin_fill()
pd()
circle(5)
end_fill()
pencolor("#000")
pu()
goto(40, -50)
pd()
pencolor("#fff")
fillcolor("#fff")
begin_fill()
goto(75, -53)
left(115)
circle(20, 240)
end_fill()
fillcolor("#824652")
pu()
goto(75, -53)
pd()
begin_fill()
pencolor("#824652")
left(123)
circle(20, 110)
left(25)
circle(20, 110)
end_fill()
pu()
goto(61, -40)
pd()
pencolor("#fff")
fillcolor("#fff")
begin_fill()
circle(5)
end_fill()
pencolor("#4D162C")
pu()
goto(82, -10)
pd()
fillcolor("#4D162C")
begin_fill()
right(140)
circle(50, 40)
goto(53, 1)
right(5)
circle(30, -95)
pu()
end_fill()
goto(-5, -5)
begin_fill()
pd()
goto(-7, 6)
left(70)
circle(45, 50)
goto(-44, -7)
right(15)
circle(50, -45)
end_fill()
colormode(255)
for i in range(1, 19):
    fillcolor(254, 234-i, 214)
    pencolor(254, 234-i, 214)
    pu()
    goto(-20, -60-i)
    pd()
    begin_fill()
    circle(20-i)
    end_fill()
for i in range(1, 19):
    fillcolor(254, 234-i, 214)
    pencolor(254, 234-i, 214)
    pu()
    goto(65, -65-i)
    pd()
    begin_fill()
    circle(20-i)
    end_fill()
pencolor("#123456")
pu()
goto(-10, -150)
pd()
goto(-5, -160)
goto(30, -153)
pu()
goto(40, -150)
pd()
goto(35, -160)
goto(0, -153)
pu()
goto(110, -230)
pencolor("#000")
write("SeeChen 2021-10-12", font=("ink free", 10))
done()
