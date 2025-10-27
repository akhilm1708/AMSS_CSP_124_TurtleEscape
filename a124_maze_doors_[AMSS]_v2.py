# ...existing code...
import turtle

num_walls = 28
path_width = 20
maze_color = "black"

wn = turtle.Screen()
wn.title("Spiral Maze with Doors")
wn.tracer(0, 0)
wn.delay(0)


maze_painter = turtle.Turtle()
maze_painter.color(maze_color)
maze_painter.hideturtle()
maze_painter.speed(0)
maze_painter.pensize(2)


maze_painter.penup()
maze_painter.goto(0, 0)
maze_painter.pendown()

wall_length = 40
door_offset = 10
door_width = path_width


for _ in range(num_walls):
    if wall_length > door_offset + door_width:
        maze_painter.forward(door_offset)
        maze_painter.penup()
        maze_painter.forward(door_width)
        maze_painter.pendown()
        maze_painter.forward(wall_length - door_offset - door_width)
    else:
        maze_painter.forward(wall_length)
    maze_painter.left(90)
    wall_length += path_width

wn.update()
wn.mainloop()