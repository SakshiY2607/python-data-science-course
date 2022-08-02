from turtle import *
speed('slow')
pencolor('blue')
bgcolor('white')
pensize(10)
size=100
side=4
fillcolor('light blue')
begin_fill()
for i in range(side):
    fd(size)
    lt(90)
    fd(size)
    rt(90)
    fd(size)
    lt(90)
end_fill()    
mainloop()    
