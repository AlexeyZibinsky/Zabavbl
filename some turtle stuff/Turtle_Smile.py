import turtle as t
import math as m

t.bgcolor("gray")

def circle1(a):
    angle=0
    while True:
        t.forward(a)
        t.left(12)
        angle += 12
        if angle == 360:
            break

def circle2(a):
    angle=0
    while True:
        t.forward(a)
        t.right(12)
        angle += 12
        if angle == 360:
            break

def make_arc(a, arc_angle):
    angle=0
    while True:
        t.forward(a)
        t.left(12)
        angle += 12
        if angle == arc_angle:
            break

def test():
    t.color("black")
    t.width(1)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(4):
        t.forward(1000)
        t.backward(1000)
        t.right(90)


#a1 = int(input())
a1 = 50
a2 = a1/10
R1 = (15*a1)/(m.pi)
R2 = (15*a2)/(m.pi)
print(R1)

t.width(2)

# Paint Yellow circle with the center in the beginning of the coords 
t.penup()
t.goto(-a1/2, -R1)
t.pendown()
t.color("yellow")
t.begin_fill()
circle1(a1)
t.end_fill()

# Paint left eye
t.penup()
t.goto(-R1/3,(R1/3)-R2)
t.pendown()
t.color("blue")
t.begin_fill()
circle1(a2)
t.end_fill()

# Paint right eye
t.penup()
t.goto(R1/3, (R1/3)-R2)
t.pendown()
t.color("blue")
t.begin_fill()
circle1(a2)
t.end_fill()

# Paint nose
t.width(20)
t.penup()
t.goto(0, R1/4)
t.pendown()
t.color("blue")
t.right(90)
t.forward(R1/4)

# Paint mouth
t.width(20)
t.penup()
t.goto(-R1/2, 0)
t.pendown()
t.color("red")
make_arc(a1/2, 180)

#test()
