#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
#Create the spider the body
spider.pensize(40)
spider.circle(20)

#Configure Spiders Legs
Legs = 8
legLength = 70
space = 360 / Legs - 20
spider.pensize(5)
n = 0
#Draw the legs
while (n < Legs):
  if n < 4:
    spider.goto(0, 20)
    spider.setheading(space * n - 45)
    spider.forward(legLength)
  else:
    spider.goto(0, 20)
    spider.setheading(space * n + 45)
    spider.forward(legLength)
  n = n + 1
#Create Eyes
spider.pensize(10)
spider.pencolor("red")
spider.fillcolor("red")
spider.penup()
spider.goto(15, 35)
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(-15, 35)
spider.pencolor("red")
spider.fillcolor("red")
spider.pendown()
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()