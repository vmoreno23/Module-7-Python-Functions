import turtle

def drawSquare(t, sz):

    for i in range(4):

        t.forward(sz)
        t.left(90)

    
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

square_side = 30
square_width = 15

for new_squares in range(5):

    drawSquare(alex, square_side)
    alex.penup()
    alex.back(square_width)
    alex.right(90)
    alex.forward(square_width)
    alex.left(90)
    alex.pendown()
    square_side = square_side + 2 * square_width

wn.exitonclick()



#Victor Moreno
#2/27/24

#Draw 5 squares within each other. Squares get smaller toward the center
