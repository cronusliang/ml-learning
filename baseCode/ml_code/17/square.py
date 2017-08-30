import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
   window =  turtle.Screen()
   window.bgcolor('green')

   n = 0
   while n < 360:
    brad = turtle.Turtle()
    brad.right(n)
    draw_triangle(brad)
    n+= 10
   window.exitonclick()

draw_art()

