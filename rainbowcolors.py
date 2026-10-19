#Display the colours of the rainbow
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Rainbow Stripes")

# Create a turtle object
rainbow = turtle.Turtle()
rainbow.speed(0)
rainbow.width(40)  # Set the width of the turtle pen to 40

# Define the rainbow colours
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Set the starting position to the left side of the screen
rainbow.penup()
rainbow.goto(-200, 100)
rainbow.pendown()

# Draw the rainbow stripes
for colour in colours:
    rainbow.color(colour)
    rainbow.forward(400)  # Move forward to the right side of the screen
    rainbow.penup()
    rainbow.backward(400)  # Move back to start position
    rainbow.right(90)
    rainbow.forward(60)  # Move down for the next stripe 
    rainbow.left(90)
    rainbow.pendown()

# Hide the turtle and display the window
rainbow.hideturtle()
screen.mainloop()