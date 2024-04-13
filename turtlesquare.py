import turtle

# Set up the screen
turtle.setup(600, 600)

# Create a turtle named "drawer"
drawer = turtle.Turtle()

# Set the speed of the turtle
drawer.speed(1)  # Speed ranges from 1 (slowest) to 10 (fastest)

# Draw a square
for _ in range(4):
    drawer.forward(100)  # Move the turtle forward 100 units
    drawer.right(90)     # Turn the turtle right by 90 degrees

# Complete drawing
turtle.done()
