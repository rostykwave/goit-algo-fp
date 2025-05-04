import turtle
import math
import sys

def iterative_pythagoras_tree(t, initial_size, initial_angle, max_level):
    """
    Draw a Pythagoras tree using an iterative approach with a stack
    instead of recursion.
    """
    # Each entry in the stack contains: (size, angle, position, heading, level)
    stack = [(initial_size, initial_angle, t.position(), 90, 0)]
    
    while stack:
        size, angle, position, heading, level = stack.pop()
        
        if level > max_level or size < 1:
            continue
            
        try:
            # Move to position and set orientation
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()
            
            # Draw the square
            t.setheading(angle)
            for _ in range(4):
                t.forward(size)
                t.left(90)
            
            # Calculate position for the branches
            t.forward(size)
            t.left(90)
            t.forward(size)
            branch_pos = t.position()
            branch_heading = t.heading()
            
            # Calculate new size for branches
            new_size = size / math.sqrt(2)
            
            # Add the right branch to stack (drawn last, so added first - LIFO)
            right_angle = angle - 45
            stack.append((new_size, right_angle, branch_pos, branch_heading - 45, level + 1))
            
            # Add the left branch to stack
            left_angle = angle + 45
            stack.append((new_size, left_angle, branch_pos, branch_heading + 45, level + 1))
            
        except turtle.Terminator:
            print("Turtle window was closed")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            # Continue with the next item in the stack instead of terminating

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
        
        # Get recursion level from user
        level_str = screen.textinput("Recursion Level", "Enter recursion level (1-10):")
        try:
            level = int(level_str)
            if level < 1:
                level = 1
            elif level > 10:
                level = 10  # Lower the max limit to ensure stability
        except (ValueError, TypeError):
            level = 6  # Lower default value
        
        # Draw the tree using iterative approach
        iterative_pythagoras_tree(t, 80, 90, level)
        
        # Update the screen at the end
        screen.update()
        
        # Keep the window open until closed
        turtle.mainloop()
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
