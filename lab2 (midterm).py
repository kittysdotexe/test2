import turtle               
import random

#Part A

window = turtle.Screen()       
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()   
leonardo = turtle.Turtle()

michelangelo.color('orange')
leonardo.color('blue')

michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()       
leonardo.up()

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here

michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(0, 10):
	michelangelo.forward(random.randrange(0,10))
	leonardo.forward(random.randrange(0,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here

michelangelo.down()

for i in range(3):
	michelangelo.forward(100)
	michelangelo.right(120)
michelangelo.clear()

for i in range(4):
	michelangelo.forward(100)
	michelangelo.right(90)
michelangelo.clear()

for i in range(6):
	michelangelo.forward(100)
	michelangelo.right(60)
michelangelo.clear()

for i in range(20):
	michelangelo.forward(100)
	michelangelo.right(18)
michelangelo.clear()

for i in range(100):
	michelangelo.forward(100)
	michelangelo.right(3.6)
michelangelo.clear()



window.exitonclick()
