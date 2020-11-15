
import turtle

stroka ="F"
rule = {"+": "+", "-": "-", "F": "F+F-F-F+F"}
def transformation(stroka = "F", **rule):
    temp_stroka = ""
    for ch in stroka:
        temp_stroka += rule[ch]
    return temp_stroka

print("our rule is F -> F+F-F-F+F")
iterations = int(input("How much iterations?"))

for i in range(iterations):
    stroka = transformation(stroka, **rule)

turtle.tracer(0,0)
turtle.penup()
turtle.setposition(-400, 350)
turtle.pendown()
turtle.speed(100000)
for ch in stroka:
    if ch == "+":
        turtle.right(90)
    elif ch == "-":
        turtle.left(90)
    else: #F
        turtle.forward(1)
turtle.update()
# Ненужный комментарий
