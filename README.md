# Akhil M and Sharvil S — Pseudocode: 1.2.4 Turtle Escape 

## Computer Science Notebook

Date: 2025-10-23
Page: 1

Goal
- Build a spiral maze using turtle graphics. Start from the center and work outward.

Decisions
- number_of_walls = 7  (chosen for this run)
- path_width = 20
- maze_color = "black"

Variables (pseudocode)
- num_walls ← 7
- path_width ← 20
- step_length ← path_width  // initial wall length
- turn_angle ← 90

Pseudocode (page-sized, iterate and grow each wall)
1. import turtle
2. create turtle object: painter
3. set painter color to maze_color
4. hide painter and lift pen as needed
5. move painter to center (start at origin)
6. pen down
7. for i in range(num_walls):
     - forward(step_length)
     - turn right(turn_angle)
     - step_length ← step_length + path_width
8. end for
9. call turtle.mainloop()  // keep window open

Notes
- Increasing step_length each iteration grows the spiral outward.
- Change num_walls to make the spiral longer or shorter.
- If needed, increase step_length only every 2 turns to form rectangular spiral spacing.




Date: 2025-10-23
Page: 2

Goal
- Add doors (openings) to spiral walls.

Decisions
- door_offset = 10
- door_width = path_width

Pseudocode (doors)
1. for i in range(num_walls):
   - wall_length ← step_length
   - if wall_length > door_offset + door_width:
       · forward(door_offset)
       · penup(); forward(door_width); pendown()
       · forward(wall_length - door_offset - door_width)
     else:
       · forward(wall_length)
   - right(90)
   - step_length ← step_length + path_width
2. turtle.mainloop()




Date: 2025-10-27
Page: 3

Goal:
- Add barriers (closed off pathways) to maze


Decisions
- barrier_offset ← 40
- barrier_length ← 2 × path_width

Pseudocode (barriers)
1. for each wall i:
   - draw door (if any)
   - if door drawn and space remains:
       · forward(barrier_offset)
       · right(90); forward(barrier_length); backward(barrier_length); left(90)
   - finish remaining wall distance
2. end for loop


Date: 2025-10-27
Page: 4

Goal:
- Fix the “too-long wall” problem.

Decisions
- outer_bound ← half of window size minus margin

Pseudocode (short)
1. for each wall i:
   - current_offset ← i × path_width
   - max_len ← outer_bound − current_offset
   - wall_length ← min(step_length, max_len)
   - if wall_length ≤ 0: break  // stop when no room remains
   - only place door/barrier if wall_length > door_offset + door_width + barrier_offset
   - draw wall using wall_length
   - step_length ← step_length + path_width
2. end for loop


PLTW Qu

Discussion 1:

The code is extremely easy to interpret because the function names follow exactly to what they do. Like you can easily understand what print_me does, and the other functions. 
Yes, all the calls to the function print_me follow the exact same logic because they all execute the identical two lines of code. 
Yes, it function print_me implements implements abstraction across all the calls. It abstracts the process of displaying a two line formatted message. 









## PLTW Questions

Discussion 2
1. Algorithms can be written in different ways and still accomplish the same task because you can execute them in different ways. You use different logics to achieve the same output, or you can use different functions. This can all lead you to the same task output. 
2. Algorithms that appear similar can yield different results because they don’t actually have the same logic. Even though they are similar those different parts of the program will lead you to a completely different output. 







 
