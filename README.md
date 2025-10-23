# Akhil M and Sharvil S — Pseudocode: 1.2.4 Turtle Escape 


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
```// filepath: c:\Users\2\Documents\GitHub\AMSS_CSP_124_TurtleEscape\README.md
// ...existing code...


