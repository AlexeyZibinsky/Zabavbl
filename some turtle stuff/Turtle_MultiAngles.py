import turtle as t
import math as m

t.shape("turtle")

l=50

for n in range(3, 14):
    l += 10
    ang = ((n-2)*180) / n
    R= 0.5*l / m.sin( m.pi*(180/n)/180 )
    print(R)
    # Придём к вершине многоугольника
    t.penup()
    t.goto(R, 0)
    t.right(180+ang/2)
    t.pendown()
    for i in range(n):
        t.forward(l)
        t.left(180-ang)
    t.left(0.5*ang + 180)
    
    

    
