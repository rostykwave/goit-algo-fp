import turtle
import math
import sys

def recursive_pythagoras_tree(t, size, angle, level):
    """
    Draw a Pythagoras tree using recursion.
    """
    if level <= 0 or size < 1:
        return
        
    try:
        # Draw the square
        t.setheading(angle)
        for _ in range(4):
            t.forward(size)
            t.left(90)
        
        # Save position for returning after drawing branches
        original_pos = t.position()
        original_heading = t.heading()
        
        # Position for branches
        t.forward(size)
        t.left(90)
        t.forward(size)
        
        # Calculate new size for branches
        new_size = size / math.sqrt(2)
        
        # Draw left branch
        recursive_pythagoras_tree(t, new_size, angle + 45, level - 1)
        
        # Return to branch position for the next branch
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.pendown()
        
        # Draw right branch
        recursive_pythagoras_tree(t, new_size, angle - 45, level - 1)
        
        # Return to original position
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.pendown()
        
    except turtle.Terminator:
        print("Turtle window was closed")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

def main():
    # Setup the screen
    try:
        screen = turtle.Screen()
        screen.title("Pythagoras Tree Fractal")
        screen.setup(800, 600)
        screen.bgcolor("white")
        screen.tracer(0)  # Turn off animation for faster drawing
        
        # Create and setup turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)  # Fastest speed
        t.penup()
        t.goto(0, -200)  # Start from bottom
        t.pendown()
        
        # Get recursion level from user
        level_str = screen.textinput("Recursion Level", "Enter recursion level (1-10):")
        try:
            level = int(level_str)
            if level < 1:
                level = 1
            elif level > 10:
                level = 10  # Limit to ensure stability
        except (ValueError, TypeError):
            level = 6  # Default value
        
        # Draw the tree using recursive approach
        recursive_pythagoras_tree(t, 80, 90, level)
        
        # Update the screen at the end
        screen.update()
        
        # Keep the window open until closed
        turtle.mainloop()
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
