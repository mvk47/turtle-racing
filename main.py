from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

bet= screen.textinput(title="Make your bet",
                 prompt= "Which turtle will win the race:\n1.Red\n2.Green\n3.Blue\n4.Yellow\n5.Orange")
print(bet)

red = Turtle()
blue = Turtle()
yellow = Turtle()
green = Turtle()
orange = Turtle()

red.color("red")
blue.color("blue")
yellow.color("yellow")
green.color("green")
orange.color("orange")


for i in (red,blue,yellow,green,orange):
    i.shape("turtle")
    i.penup()
race_on=False

red.goto(x=-230,y=-100)
blue.goto(x=-230,y=-70)
yellow.goto(x=-230,y=-40)
green.goto(x=-230,y=-10)
orange.goto(x=-230,y=20)



if bet:
    race_on=True
while race_on:
    for i in (red,blue,yellow,green,orange):
        if i.xcor()>230:
            race_on=False
            winning_color = i
            print("And the winning color is.....",winning_color.pencolor())
            if winning_color==bet:
                print("You have won my friend. Let there be a legend...")
            else:
                print("Another looser!!!")
        rand_distance = random.randint(0,10)
        i.forward(rand_distance)








screen.exitonclick()
