from math import pi

file = open(file='elso.txt', mode='w', encoding='utf-8')

file.write('Hello, this is my first txt file! uwu\n')
name:str = 'Juhász Zoltán'
file.write(f'My name is {name}\n')

file.write(f'Pi = {pi}')

print('done!')