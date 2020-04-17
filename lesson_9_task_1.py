import random

while True:
    question = input('Введите вопрос: ')
    print(f'{question} ', random.choice(['Да', 'Нет']))
