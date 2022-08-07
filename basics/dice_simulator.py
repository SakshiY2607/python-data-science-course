from random import randint
win_count=0
lose_count =0
dice =['1','2','3','4','5','6']
n=0
while True:
    input('press enter to 🎲roll dice')
    out=randint(1,6)

    print(f'🎲 =>{dice[out-1]}') #use run and debug for dry run
    for i in range(0,n):
        if out==6:
            win_count +=1
        elif out==1:
               lose_count+=1
    n=n+1       

    if win_count==3:
        print('you win 👑')  
        break
    elif lose_count ==3:
        print('you lose 💀')  
        break
else:
        print('get lost 🛴')



