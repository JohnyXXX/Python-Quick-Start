"""
Сделать так, чтобы она помнила
отвеченные вопросы
"""
import random

storage_db = []


def answer():
    x = random.choice(['Да', 'Нет'])
    return x


for i in range(10):
    question = input('Введите вопрос: ')
    q_a = (question, answer())
    print('Ответ:', q_a[1])
    storage_db.append(q_a)
