from turtle import Turtle, tracer
from time import clock

class Stack:
     def __init__(self):
         self.stuff = []

     def isEmpty(self):
         return bool(self.stuff)

     def push(self, item):
         self.stuff.append(item)

     def pop(self):
         return self.stuff.pop()

def getExpr(axiom, iterations, rules):  #generates the expression
    start = axiom
    for i in range(iterations-1):
        for j in rules:
            start = start.replace(j ,rules[j])
    return start

def draw(axiom, angle, iterations, rules, d=8): #gets the expression and draws it
    stack = Stack()
    turtle = Turtle()
    
    turtle.seth(90)
    turtle.penup()
    turtle.setposition(0,-350)
    turtle.pendown()
    turtle.speed(0)
    tracer(500,500) #change this to alter speed, currently set to not too fast, not too slow
    turtle.pensize(2)
    
    for i in getExpr(axiom, iterations, rules):
        if i == "F":
            turtle.fd(d)
        if i == "-":
            turtle.rt(angle)
        if i == "+":
            turtle.lt(angle)
        if i == "[":
            stack.push((turtle.pos(), turtle.heading()))
        if i == "]":
            turtle.penup()
            popped = stack.pop()
            turtle.setpos(popped[0])
            turtle.setheading(popped[1])
            turtle.pendown()

def q0():
    draw("F", 25.7, 5, {"F":"F[+F]F[-F]F"})

def q1():
    draw("F", 20, 6, {"F":"F[+F]F[-F][F]"},12)

def q2():
    draw("F", 22.5, 5, {"F":"FF-[-F+F+F] + [+F-F-F]"}, 12)

def q3():
    draw("X", 20, 7, {"F":"FF", "X":"F[+X]F[-X]+X"}, 6)
    
def q4():
    draw("X", 25.7, 7, {"F":"FF", "X":"F[+X][-X]FX"}, 6)
    
def q5():
    draw("X", 22.5, 5, {"F":"FF", "X":"F-[[X]+X]+F[+FX]-X"}, 15)
