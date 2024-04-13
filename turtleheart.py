import turtle

# Set up the screen
turtle.setup(800, 600)
screen = turtle.Screen()
screen.title("Heart with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.fillcolor("red")
drawer.begin_fill()

# Start drawing the heart
drawer.left(50)
drawer.forward(133)
drawer.circle(50, 200)
drawer.right(140)
drawer.circle(50, 200)
drawer.forward(133)

drawer.end_fill()
# Hide the turtle after drawing
drawer.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()
