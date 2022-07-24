from turtle import *
speed('slow')
pencolor('black')
bgcolor('light blue')
pensize(10)
size=100
side=4
fillcolor ='white'
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
