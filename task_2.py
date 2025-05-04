import turtle
import math

def draw_pythagoras_tree(t, size, angle, level):
    """
    Recursively draw a Pythagoras tree.
    
    Args:
        t: Turtle object
        size: Size of the square
        angle: Current angle of the turtle
        level: Recursion level
    """
    if level == 0:
        return
    
    # Save the current state
    t.pendown()
    t.setheading(angle)
    
    # Draw the square
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    # Calculate positions for the branches
    t.forward(size)
    t.left(90)
    t.forward(size)
    pos = t.position()
    heading = t.heading()
    
    # Calculate new size for branches
    new_size = size / math.sqrt(2)
    
    # First branch (45 degrees to the left)
    t.left(45)
    draw_pythagoras_tree(t, new_size, angle + 45, level - 1)
    
    # Return to position for the second branch
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()
    
    # Second branch (45 degrees to the right)
    t.right(45)
    draw_pythagoras_tree(t, new_size, angle - 45, level - 1)
    
    # Return to the original position
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.right(180)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(180)
    t.pendown()

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.setup(800, 600)
    screen.bgcolor("white")
    
    # Create and setup turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    t.penup()
    t.goto(0, -200)  # Start from bottom
    t.pendown()
    
    # Get recursion level from user
    level_str = screen.textinput("Recursion Level", "Enter recursion level (1-12):")
    try:
        level = int(level_str)
        if level < 1:
            level = 1
        elif level > 12:
            level = 12  # Limit to avoid excessive calculations
    except (ValueError, TypeError):
        level = 8  # Default value
    
    # Draw the tree
    draw_pythagoras_tree(t, 80, 90, level)  # Start with angle 90 (pointing up)
    
    # Keep the window open until closed
    turtle.mainloop()

if __name__ == "__main__":
    main()
