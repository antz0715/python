import turtle

# Set up the screen
turtle.setup(600, 600)

# Create a turtle named "drawer"
drawer = turtle.Turtle()

# Set the speed of the turtle
drawer.speed(1)  # Speed ranges from 1 (slowest) to 10 (fastest)

# Move the turtle to a starting position
drawer.penup()  # Don't draw when moving to the start position
drawer.goto(-50, 50)  # Move the turtle to this position before starting to draw
drawer.pendown()  # Start drawing

# Draw a square
for _ in range(4):
    drawer.forward(100)  # Move the turtle forward 100 units
    drawer.right(90)     # Turn the turtle right by 90 degrees

# Complete drawing
turtle.done()
