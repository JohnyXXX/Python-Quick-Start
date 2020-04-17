"""
Написать программу, которая на
любой вопрос отвечает "да" или "нет"
"""
import random


def answer():
    x = random.choice(['Да', 'Нет'])
    return x


for i in range(10):
    question = input('Введите вопрос: ')
    print('Ответ:', answer())
