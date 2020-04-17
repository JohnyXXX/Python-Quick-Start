"""
Сделать так, чтобы она помнила
отвеченные вопросы
"""
import random

storage_db = []


def answer():
    x = random.choice(['Да', 'Нет'])
    return x


def check_answer(q):
    if not storage_db:
        q_a = (q, answer())
        storage_db.append(q_a)
        return q_a
    else:
        for x in storage_db:
            if q == x[0]:
                return x
            else:
                continue
        q_a = (q, answer())
        storage_db.append(q_a)
        return q_a


for i in range(10):
    question = input('Введите вопрос: ')
    print('Ответ:', check_answer(question)[1])
