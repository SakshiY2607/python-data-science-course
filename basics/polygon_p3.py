from tkinter import N
from turtle import *
speed('fast')
pencolor('red')
bgcolor('light blue')
size=100
side=4
fillcolor('red')
begin_fill()
#for i in range(size):
  #  fd(i*2)
 #   lt(90)
#mainloop()    
  

#second way
n=10
lt(180)
for i in range(size):
    fd(n)
    rt(90)
    write('||||')
    n=n+2
mainloop()

