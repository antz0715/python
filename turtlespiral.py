import turtle

turtle.speed(0)  # Set the speed to the fastest

for i in range(100):
    turtle.forward(i)
    turtle.right(20)  # Adjust angle for tighter or looser spiral

turtle.done()
