import turtle

turtle.speed(0)

for i in range(10):
    turtle.circle(10 * i)
    turtle.up()  # Move turtle without drawing
    turtle.sety(-10 * i)  # Move the turtle down to keep circles centered
    turtle.down()

turtle.done()
