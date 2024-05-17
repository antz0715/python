import turtle

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

turtle.speed(1)

draw_polygon(10, 100)  # Draw a pentagon

turtle.done()
