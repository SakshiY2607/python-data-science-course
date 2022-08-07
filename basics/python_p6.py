from turtle import *
speed('slow')
pencolor('red')
bgcolor('light blue')
fillcolor('red')
begin_fill()
n=30
for i in range(3):
    dot(20)
    penup()
    goto(n,0)
    n=n+30
    pendown()
for i in range(2):
    penup()
    goto(n-60,-30)
    dot(20)
    pendown()
mainloop()