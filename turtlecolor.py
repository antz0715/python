import turtle

colors = ['red', 'blue', 'green', 'yellow', 'purple']

turtle.speed(10)

for i in range(36):
    turtle.color(colors[i % len(colors)])  # Change color
    turtle.forward(100)
    turtle.right(170)

turtle.done()
