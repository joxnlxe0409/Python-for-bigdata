import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

square(100)
square(200)
square(300)

turtle.done()
