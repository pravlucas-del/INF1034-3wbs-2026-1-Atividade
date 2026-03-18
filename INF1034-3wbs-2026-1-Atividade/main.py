from turtle import *

t = Turtle()
# Começo do plano cartesiano
t.goto(-300,0)
t.pu()
t.goto(0,0)
t.pd()

t.goto(300,0)
t.stamp()
t.pd()


t.goto(0,0)
t.pd()
t.goto(0,-300)
t.pd()
t.goto(0,0)
t.pd()
t.goto(0,300)
t.pd()
t.left(90)
t.stamp()
t.rt(90)
# Plano cartesiano feito

color = textinput("Obter cor", "Digite a cor:")
t.color("red")
t.begin_fill()
t.fillcolor(color)
t.pu()
t.goto(200,100)
t.pd()

for _ in range(8):
    
    t.fd(100)
    t.left(45)

t.end_fill()

color = textinput("Obter cor", "Digite a cor:")
t.color("blue")
t.begin_fill()
t.fillcolor( color)
t.pu()

t.goto(-200,100)
t.pd()
for _ in range(3):
    t.fd(100)
    t.lt(120)

t.end_fill()
color = textinput("Obter cor", "Digite a cor:")
t.color("purple")
t.begin_fill()
t.fillcolor(color)

t.pu()
t.goto(-200,-300)
t.pd()
for _ in range(12):
    t.fd(50)
    t.left(30)
t.end_fill() 
color = textinput("Obter cor", "Digite a cor:")
t.color("grey")
t.begin_fill()
t.fillcolor( color)
t.pu()
t.goto(300,-350)
t.pd()
for _ in range(5):
    t.fd(100)
    t.lt(72)
t.end_fill()

#Spiral farm aura
color = textinput("Obter cor", "Digite a cor:")
t.color("black")
t.begin_fill()
t.fillcolor( color)
t.pu()
t.goto(150,-100)
t.pd()
t.speed(0)
for i in range(40):
    t.fd(i*2)
    t.lt(45)


mainloop()
