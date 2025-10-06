import turtle as t

screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)

t.title("Turtle Star Flower Diagram")
t.color("red","yellow")
t.begin_fill()
t.speed(0)

while True:
    t.forward(400)
    t.left(170)

    if abs(t.position()) < 1:
        break

t.end_fill()
t.exitonclick()
