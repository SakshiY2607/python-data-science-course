class Cat:
    breed=None
    gender=None
    fur_color =None
    age=None
    height=None
    weight=None
    is_tamed=None
    def eat(self, food='catfood'):#by using self keyword that this denotes that the function is of class given ...we don't need to pass this function its by default pass
        print(f'🐈is eating{food}')
    def play(self):
        print('🐈 is playing')
    def sleep(self):
        print('🐈 is sleeping')       
billu=Cat()#constructor calling
tom=Cat()
bagadbilla=Cat()
billu.breed='persian'
billu.weight=2
billu.age=2
billu.fur_color='white'
billu.height=1
billu.is_tamed=True
billu.gender='M'

tom.breed='street cat'
tom.weight=1.5
tom.age=100
tom.fur_color='grey'
tom.height=1.1
tom.is_tamed=True
tom.gender='M'

bagadbilla.breed='wild cat'
bagadbilla.weight=2
bagadbilla.age=4
bagadbilla.fur_color='black'
bagadbilla.height=1.2
bagadbilla.is_tamed=False
bagadbilla.gender='M'

print('Billu details')
print('breed:',billu.breed)
print('gender:',billu.gender)
print('age:',billu.age)
print('weight:',billu.weight)
print('height:',billu.height)
print('color:',billu.fur_color)
print('pet:','yes' if billu.is_tamed else'no')
billu.eat()
billu.sleep()
billu.play()

print('tom details')
print('breed:',tom.breed)
print('gender:',tom.gender)
print('age:',tom.age)
print('weight:',tom.weight)
print('height:',tom.height)
print('color:',tom.fur_color)
print('pet:','yes' if tom.is_tamed else'no')
tom.sleep()
tom.play()
tom.sleep()

print('Bagadbilla details')
print('breed:',bagadbilla.breed)
print('gender:',bagadbilla.gender)
print('age:', bagadbilla.age)
print('weight:',bagadbilla.weight)
print('height:',bagadbilla.height)
print('color:',bagadbilla.fur_color)
print('pet:','yes' if bagadbilla.is_tamed else'no')
bagadbilla.eat('mouse')
bagadbilla.eat('bird')
bagadbilla.sleep()
bagadbilla.eat('bird')





