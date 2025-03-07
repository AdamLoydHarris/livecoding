# %%
# import turtle

# window = turtle.Screen()
# window.title("Turtle Test")

# # Create a turtle named "my_turtle"
# my_turtle = turtle.Turtle()
# my_turtle.color("blue")
# my_turtle.pensize(5)
# my_turtle.shape("turtle")

# # Move the turtle forward
# my_turtle.forward(100)

# # Close the window when clicked
# window.exitonclick()

# %%
# import turtle

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# t = turtle.Pen() 
# f = [500, 200, 100, 50]

# turtle.bgcolor('black') 
# turtle.speed(0)

# t.penup()

# # Move the turtle to the desired starting position
# t.goto(-200, 400)  # Move to coordinates (-100, 50)

# # Put the pen down to start drawing
# t.pendown()

# for x in range(360): 
#     t.pencolor('white') 
#     t.width(x//100 + 1) 
#     t.forward(f[x%4]) 
#     t.left(150) 
# window.exitonclick()
# %%
# import turtle
# import colorsys

# # Create window to Display Pattern
# t = turtle.Turtle()
# s = turtle.Screen()

# # Setting Background color
# s.bgcolor("black")

# # Speed of turtle to draw pattern
# t.speed(0)

# n = 36
# h = 0

# # Loop for drawing Pattern
# for i in range(300):
#     c = colorsys.hsv_to_rgb(h,1,0.9)
#     h+=1/n
#     t.color(c)
#     t.left(155)
#     for j in range(5):
#         t.forward(300-i)
#         t.left(150)


#%%
import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the pen width

# Define the colors to be used in the pattern
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Function to draw a hexagon
def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)

# Draw the hexagonal spiral
for i in range(60):
    t.color(colors[i % 6])  # Cycle through the colors
    draw_hexagon(i * 5)     # Increase the size of the hexagon
    t.left(10)              # Rotate slightly for the next hexagon

# Complete the drawing and keep the window open
turtle.done()
