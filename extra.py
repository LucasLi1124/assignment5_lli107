import turtle

def draw_ring(color, x, y):
    """
    Draw a ring with the specified color at the given (x, y) position.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(50)

def main():
    # Set up the screen
    turtle.setup(800, 400)
    turtle.title("Olympic Rings")

    # Set the speed of drawing
    turtle.speed(5)

    # Draw the rings
    draw_ring("blue", -120, 0)
    draw_ring("black", 0, 0)
    draw_ring("red", 120, 0)
    draw_ring("yellow", -60, -50)
    draw_ring("green", 60, -50)

    # Hide the turtle and display the window
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
