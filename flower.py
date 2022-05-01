import turtle

flower = turtle.Turtle()
flower.color("yellow", "orange")
flower.begin_fill()
for i in range(12):
    flower.forward(350)
    flower.right(150)
flower.end_fill()



turtle.done()