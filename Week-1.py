#Section 1
name= 'max'
age= 14
height= 5.2
is_student= False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name= input('What\'s your name? ')
year= int(input('What year were you born? '))
age= 2026-year

print(f'Hi, {name}! You are {age} years old.')

#Section 3
dogs= input('How many dogs do you have? ')
cats= input('How many cats do you have? ')
total= float(dogs)+float(cats)

print('You have: ' + str(total) + ' pets!')

#Section 4
item= ('Twin Bed')
price= 500
quantity= 4
total= (price*quantity)

print()
print('===========================')
print('          RECEIPT          ')
print('===========================')
print(f'Item:             {item}')
print(f'Price:            {price}')
print(f'Quantity:         {quantity}')
print('---------------------------')
print(f'Total:            {total}')
print('===========================')

#Section 5
name= input('Hello, please enter your name: ')
town= input('What\'s your hometown? ')
hobby= input('Your favorite hobby? ')
fact= input('What\'s 1 fact about you? ')
year= int(input('Lastly, what year were you born? '))

age= 2026-year

print()
print('╔══════════════════════════════╗')
print(f'        PROFILE:{name}      ')
print('╚══════════════════════════════╝')
print(f'Hometown~         {town}')
print(f'Hobby~            {hobby}')
print(f'Fun Fact~         {fact}')
print(f'Age~              {age}')
