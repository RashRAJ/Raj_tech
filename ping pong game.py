import turtle

wn = turtle.Turtle()
wn = turtle.Screen()
wn = turtle.bgcolor("black")


tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.goto(200, 200)
tim.pendown()
tim.color("pink")
tim.width(10)
tim.speed(10)
for i in range(50):
    tim.forward(300)
    tim.left(170)


tim1 = turtle.Turtle()
tim1.penup()
tim1.hideturtle()
tim1.goto(-200, 200)
tim1.pendown()
tim1.color("#f37736")
tim1.width(10)
tim1.speed(10)
for i in range(50):
    tim.forward(300)
    tim.left(170)

pen = turtle.Turtle()
pen.color("#f9caa7")
pen.penup()
pen.hideturtle()
pen.goto(0, 90)
pen.write("Happy", align="center", font=("Times", 20, "bold italic"))
pen.goto(0, 20)
pen.write("Birthday", align="center", font=("Times", 30, "bold italic"))
pen.goto(30, 30)
pen.write("Moha!!!!!", align="right", font=("Times", 20, "bold italic"))
