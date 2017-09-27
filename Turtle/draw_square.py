import turtle

# create function to draw a sqare. takes a turtle as a argument
def draw_sqaure(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    # Create an instance of Turtle "brad"
    brad = turtle.Turtle() 
    brad.shape("triangle")
    brad.color("pink")
    brad.speed(5)
    for i in range(0,35):
        draw_sqaure(brad)
        brad.right(10)
    #Create instance of Turtle "angie"
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.circle(100)
    

    window.exitonclick()

draw_art()
