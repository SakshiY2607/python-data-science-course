for i in range(1000,16000):
    print(f'{i} {chr(i)}' , end='\t\t') #end='\t\t' is for space 
    if i%10==0:
        print()