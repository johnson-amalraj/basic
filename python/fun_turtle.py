import turtle
# Make square using turtle 

# Take instance for turtle in the name of john
john = turtle.Turtle()
john.speed(10);

# Define a function
def make_square():
    # john.pensize(10)
    john.color("red")
    john.forward(100)
    john.right(90)
    john.color("orange")
    john.forward(100)
    john.right(90)
    john.color("blue")
    # john.pensize(20)
    john.forward(100)
    john.color("black")
    john.right(90)
    john.forward(100)

# Call a function
make_square()
john.forward(100)
make_square()