import turtle              
import random

window = turtle.Screen()       
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()   
leonardo = turtle.Turtle()

def turtleSetUp():
  '''
   Sets up Turtles.
   No args.
   No return value.
  '''
 
  michelangelo.color('orange')
  leonardo.color('blue')

  michelangelo.shape('turtle')
  leonardo.shape('turtle')

  michelangelo.up()       
  leonardo.up()

  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)

  michelangelo.forward(random.randrange(1,100))
  leonardo.forward(random.randrange(1,100))

  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)


def labTwoPartA(randomRange):
  '''
   Races the two Turtles.
   Argument is randomRange.
   No return value.
  '''
 
  for i in range(0, 10):
    michelangelo.forward(random.randrange(0,randomRange))
    leonardo.forward(random.randrange(0,randomRange))

  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)

  michelangelo.down()

def askUser():
 '''
  Asks User for Shape Length.
  No args.
  Returns shapeLength.
 '''  
 shapeLength = int(input("Length of Shape?"))
 return shapeLength

def labTwoPartB():
  '''
   Draws Shapes.
   No args.
   No return value.
  '''

  shapeLength = int(askUser())
  for i in range(3):
    michelangelo.forward(shapeLength)
    michelangelo.right(120)
  michelangelo.clear()

  for i in range(4):
    michelangelo.forward(shapeLength)
    michelangelo.right(90)
  michelangelo.clear()

  for i in range(6):
    michelangelo.forward(shapeLength)
    michelangelo.right(60)
  michelangelo.clear()

  for i in range(20):
    michelangelo.forward(shapeLength)
    michelangelo.right(18)
  michelangelo.clear()

  for i in range(100):
    michelangelo.forward(shapeLength)
    michelangelo.right(3.6)
  michelangelo.clear()
def askShape():
  ''' 
   Asks user what shape to draw at what length. )
   No arguments.
   No return value.
  '''
  
  count = 0
  michelangelo.down()
  while(count == 0): 
   shape = input("What shape should I draw? (Triangle, Square, Circle):")
   shapeLength = int(input("Length of " + str(shape) + "?"))
   
   if shape == "Triangle":
     for i in range(3):
       michelangelo.forward(shapeLength)
       michelangelo.right(120)
       count += 1
   elif shape == "Square":
     for i in range(4):
       michelangelo.forward(shapeLength)
       michelangelo.right(90)
       count += 1
   elif shape == "Circle":
      michelangelo.circle(shapeLength)
      count += 1
   else:
      print("This is not a valid shape! (remember, case sensitive!) Try again.")
  print("I like your shape. Good choice.")

def main():
 turtleSetUp()
 labTwoPartA(100)
 labTwoPartB()
 askShape()

main()

window.exitonclick()
