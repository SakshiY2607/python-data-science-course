x='sophomore'
print(x[0],x[2])
print(x[-3])
print([x[-9],x[0]])
 #print(x[10])

#accessing string characters in python
str='digipodium'
print('str=',str)
#first character
print('str=',str[0])
#second character
print('str=',str[1])
#last character
print('str=',str[-1])
#second last character
print('str=',str[-2])
#slicing
print(str[2:8]) #slicing means taking a specific portion of ur choice as output from the given string[starting index : ending index]
#for eg 
slice1=str[0:7]#slice 1 n slice 2 means the same
slice2=str[:7]
print(slice1 ,',' , slice2)
print(str[0:4])
print(str[-8:-2])#this will work only if the index specified are in inverse order i.e it will work for -8:-2 but would not work for -2:-8
#getting a slice
slice4=str[4:len(str)]#slice4 n slice5 will produce same output
slice5=str[4:]
print(slice4,'/', slice5)
x='EXCELLENT'
print(x[-4:])

