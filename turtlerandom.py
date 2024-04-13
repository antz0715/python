import turtle
import random

turtle.speed(0)

for _ in range(100):
    turtle.setheading(random.choice([0, 90, 180, 270]))  # Choose a random direction
    turtle.forward(20)

turtle.done()
