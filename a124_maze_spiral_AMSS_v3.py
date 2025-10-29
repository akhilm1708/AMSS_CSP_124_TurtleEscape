
import turtle
import random

num_walls = 16
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
draw_bool = [True, False]
count = 0


for wall_count in range(num_walls):
  
    if random.choice(draw_bool) and wall_length > door_offset + door_width:
        
        maze_painter.forward(door_offset)
        maze_painter.penup()
        maze_painter.forward(door_width)
        maze_painter.pendown()

        maze_painter.forward(wall_length - door_offset - door_width)
    else:
        maze_painter.forward(wall_length)

    if wall_count > 4 and wall_count <= (num_walls - 4):
        if random.choice(draw_bool):
            maze_painter.right(90)
            maze_painter.forward(path_width * 2)
            maze_painter.backward(path_width * 2)
            maze_painter.left(90)

    maze_painter.left(90)
    wall_length += path_width
    

wn.update()
wn.mainloop()