"""
Сделать так, чтобы она помнила
отвеченные вопросы
даже переформулированные
"""

from lesson_9_task_3_module import Head

head = Head()
question = ''

while question != 'стоп':
    answer = head.think(input('Какой вопрос? '))
    print(answer)
