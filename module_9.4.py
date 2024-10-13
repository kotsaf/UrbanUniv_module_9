"""Lambda-функция"""
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

'''
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
'''



"""Замыкание"""
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

'''
Это строчка
['А', 'это', 'уже', 'число', 5, 'в', 'списке']
'''



"""Метод __call__"""
from random import choice

class MysticBall:

    def __init__(self, *balls):
        self.balls = balls

    def __call__(self):
        return random.choice(self.balls)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

'''
Наверное
Да
Наверное
'''
