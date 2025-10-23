import turtle

num_walls = 7
path_width = 20
maze_color = "black"

maze_painter = turtle.Turtle()
maze_painter.color(maze_color)
maze_painter.hideturtle()



for _ in range(num_walls):
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width*2)
    maze_painter.pendown()

    maze_painter.forward(40)
    maze_painter.right(90)
    maze_painter.forward(path_width*2)
    maze_painter.back(path_width*2)
    maze_painter.left(90)

    wn = turtle.Screen()
    wn.mainloop()
