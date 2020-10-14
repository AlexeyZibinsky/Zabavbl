import turtle

stroka ="F-G-G"
rule = {"+": "+",
        "-": "-",
        "F": "F-G+F+G-F",
        "G": "GG"}
angle = 120
def transformation(stroka, **rule):
    temp_stroka = ""
    for ch in stroka:
        temp_stroka += rule[ch]
    return temp_stroka

iterations = int(input("How much iterations?"))

for i in range(iterations):
    stroka = transformation(stroka, **rule)

turtle.tracer(0)
turtle.penup()
turtle.setposition(-200, -250)
turtle.pendown()
for ch in stroka:
    if ch == "+":
        turtle.right(angle)
    elif ch == "-":
        turtle.left(angle)
    else: #F or G
        turtle.forward(10)
turtle.update()
turtle.mainloop()
