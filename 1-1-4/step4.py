import turtle as trtl

color1 = "blue"

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 100 # the radius of the circle
angle = 90 # experiment
seg = int(360/angle) # the length of a line

start_loop = 'n'

while (start_loop == 'y'):
  painter.right(angle)
  painter.forward(space)
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()

wn = trtl.Screen()
wn.mainloop()
# wn.bye() # new method to close the turtle window
