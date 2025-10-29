#Akhil Muthyala and Sharvil Suresh Final 1.2.4 Code

#All questions from PLTW + documentation from are in README.md


# Setup:
import turtle
import time
import random

num_walls = 12  
path_width = 30  
maze_color = "black"

wn = turtle.Screen()
wn.title("Spiral Maze with Doors")
wn.delay(0)


#Turtle objects initialization:
maze_painter = turtle.Turtle()
maze_painter.color(maze_color)
maze_painter.speed('fastest')
maze_painter.pensize(2)
maze_painter.hideturtle()

maze_runner = turtle.Turtle()
maze_runner.color("red")  
maze_runner.speed(0)  
maze_runner.shape("turtle")  
maze_runner.pensize(3)  
maze_runner.penup()
maze_runner.goto(-30, -30)  


#Movement functions:
def move_up():
    """Set maze_runner heading to up (0 degrees)"""
    maze_runner.setheading(90)
    move_runner(15)
    
def move_down():
    """Set maze_runner heading to down (180 degrees)"""
    maze_runner.setheading(270)
    move_runner(15)

def move_left():
    """Set maze_runner heading to left (270 degrees)"""
    maze_runner.setheading(180)
    move_runner(15)

def move_right():
    """Set maze_runner heading to right (90 degrees)"""
    maze_runner.setheading(360)
    move_runner(15)

 

def toggle_trail():
    """Toggle pen up/down to control trail drawing"""
    if maze_runner.isdown():
        maze_runner.penup()
    else:
        maze_runner.pendown()


#Loop setup:
maze_painter.penup()
maze_painter.goto(0, 0)
maze_painter.pendown()

wall_length = 40
door_offset = 10
door_width = path_width
draw_bool = [True, False]
count = 0


#Drawing door and barrier functions:
def draw_door(door_position):
    """Draw a door at the specified position"""
    maze_painter.forward(door_position)
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()


def draw_barrier(barrier_length):
    """Draw a barrier perpendicular to the current direction"""
    maze_painter.right(90)
    maze_painter.forward(barrier_length)
    maze_painter.backward(barrier_length)
    maze_painter.left(90)



for wall_count in range(num_walls):
  
    if (wall_count > 4 and wall_count <= (num_walls - 4)
        and random.choice(draw_bool)
        and wall_length > door_offset + door_width):
        draw_door(door_offset)
        maze_painter.forward(wall_length - door_offset - door_width)
    else:
        maze_painter.forward(wall_length)

    if wall_count > 4 and wall_count <= (num_walls - 4):
        if random.choice(draw_bool):
            draw_barrier(path_width * 2)


    maze_painter.left(90)
    wall_length += path_width
    



# Timer, escape detection, and restart functions:
start_time = None
maze_bound = None  

"""Timer state and helpers (no CLI prints, no HUD)."""

def restart_game():
    global start_time
    maze_runner.clear()
    maze_runner.penup()
    maze_runner.goto(-30, -30)
    maze_runner.setheading(90)
    maze_runner.pendown()
    start_time = None


def start_timer_if_needed():
    global start_time
    if start_time is None:
        start_time = time.time()

def check_escape_and_restart():
    if maze_bound is None:
        return
    x, y = maze_runner.position()
    if abs(x) > maze_bound or abs(y) > maze_bound:
        restart_game()

#Move runner function:
def move_runner(amount):
    """Move the maze runner forward by the specified amount"""
    start_timer_if_needed()
    maze_runner.forward(amount)
    check_escape_and_restart()


# Key event handling:
wn.onkeypress(lambda: move_up(), "Up")
wn.onkeypress(lambda: move_down(), "Down")
wn.onkeypress(lambda: move_left(), "Left")
wn.onkeypress(lambda: move_right(), "Right")
wn.onkeypress(lambda: toggle_trail(), "g")
wn.onkeypress(lambda: restart_game(), "r")
wn.listen()

# no HUD timer loop

wn.mainloop()