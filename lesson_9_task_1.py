"""
Написать программу, которая на
любой вопрос отвечает "да" или "нет"
"""
import random


def answer():
    x = random.choice([0, 1])
    if x == 0:
        return 'Нет'
    else:
        return 'Да'


for i in range(10):
    question = input('Введите вопрос: ')
    print('Ответ:', answer())
