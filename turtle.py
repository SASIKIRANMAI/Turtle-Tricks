import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
colors = ["red","orange","yellow","green","blue","indigo","violet"]
for i in range(300):
    my_turtle.pencolor(colors[i%7])
    my_turtle.forward(3*i)
    my_turtle.right(190)
turtle.done()
