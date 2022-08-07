from turtle import *

speed('slowest') #for speed control
pencolor('red') #works similar to color() 
bgcolor('light blue') #background color
color('green')
side=3
size=200
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()