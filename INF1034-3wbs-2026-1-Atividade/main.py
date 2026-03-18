from turtle import *

t = Turtle()
# Começo do plano cartesiano
t.goto(-300,0)
t.pu()
t.goto(0,0)
t.pd()

t.goto(300,0)
t.pd()

t.goto(0,0)
t.pd()
t.goto(0,-300)
t.pd()
t.goto(0,0)
t.pd()
t.goto(0,300)
t.pd()
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
t.goto(200,-300)
t.pd()
for _ in range(5):
    t.fd(100)
    t.lt(72)
t.end_fill()



mainloop()
