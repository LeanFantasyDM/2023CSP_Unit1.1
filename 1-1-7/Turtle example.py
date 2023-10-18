import turtle as trtl

jack = trtl.Turtle()
quandalatavious = trtl.Turtle()
ryan = trtl.Turtle()
james = trtl.Turtle()
josh = trtl.Turtle()
zach = trtl.Turtle()

turtlelist = (ryan, jack, quandalatavious, james, josh, zach)

x = -100
y = 0

for turtle in turtlelist:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 10

print(turtlelist)
wn = trtl.Screen()
wn.mainloop()
