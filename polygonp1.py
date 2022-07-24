from turtle import *

speed('slow') #for speed control
pencolor('red') 
bgcolor('light blue') #background color
pensize(10) #bold sides

side=3
size=200
fillcolor('green')
begin_fill() #befin fill
for i in range(side):
    fd(size)
    lt(360/side)
    
end_fill()#end the color filling

mainloop()