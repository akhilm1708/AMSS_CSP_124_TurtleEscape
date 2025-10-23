import turtle

num_walls = 7
path_width = 20
maze_color = "black"

maze_painter = turtle.Turtle()
maze_painter.color(maze_color)
maze_painter.hideturtle()

maze_painter.forward(10)
maze_painter.penup()
maze_painter.forward(path_width*2)
maze_painter.pendown()