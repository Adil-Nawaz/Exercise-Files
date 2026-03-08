
#Event listeners in python
'''
from turtle import Turtle, Screen


tim = Turtle()
tim.color("Blue")
tim.shape("turtle")

def moveForward():
    tim.forward(100)




screen = Screen()
screen.listen() #mendatory for listening any event
screen.onkey(key="space",fun=moveForward)              
#moveForward is used as argument inside onKey() function so we dont use () with moveforward because we want to trigger it everytime
#when an associated key like space key is pressed each time


screen.exitonclick()


#Etch a sketch app
from turtle import Turtle, Screen


tim = Turtle()
tim.color("Blue")
tim.shape("turtle")

def moveForward():
    tim.forward(10)
def movebackward():
    tim.backward(10)
def clockWise():
    tim.right(10)
def anticlockWise():
    tim.left(10)
def clearScreen():
    tim.home()
    tim.clear()
    

screen = Screen()
screen.listen() #mendatory for listening any event
screen.onkey(key="w",fun=moveForward)              
screen.onkey(key="s",fun=movebackward)              
screen.onkey(key="a",fun=anticlockWise)              
screen.onkey(key="d",fun=clockWise)
screen.onkey(key="c",fun=clearScreen)


screen.exitonclick()
'''

#Object state and instances
from turtle import Turtle, Screen
import random
is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtles = []
ypos = -100


screen = Screen()
screen.setup(width=500, height=400) #used to setup width and height of screen
userChoice = screen.textinput(title="Which turtle going to win the race?", prompt="Enter the color: ")
#textinput() used to take input from user on dialogue box

for i in range(0, len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.pu()
    t.goto(x=-230, y=ypos)
    ypos += 40
    turtles.append(t)

if userChoice:
    is_race_on = True

while is_race_on:
    for allTurtles in turtles:
        if allTurtles.xcor() > 230:
            is_race_on = False
            winningTurtle = allTurtles.pencolor()
            if winningTurtle == userChoice:
                print(f"You have won. The {winningTurtle} turtle won!")
            else:
                print(f"You have lost. The {winningTurtle} turtle won.")
        randomDist = random.randint(0,10)
        allTurtles.forward(randomDist)


screen.exitonclick()