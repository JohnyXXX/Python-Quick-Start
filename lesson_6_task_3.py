'''
Сделать поиск нечетким
наташа = нташа = Наташа
120 = 121 = 118
'''

from itertools import product
from pprint import pprint

from lesson_6_task_3_module import compare, int_val

NAME_WORDS = {'имя', 'зовут'}
HEIGHT_WORDS = {'рост', 'выше', 'ниже'}
WEIGHT_WORDS = {'вес', 'тяжелее', 'легче', 'весит'}


class Person:
    def __init__(self, name, birth_date, sex, height, weight):
        self.name, self.birth_date, self.sex, self.height, self.weight = name, birth_date, sex, height, weight
        self.key = (name, birth_date)

    def __repr__(self):
        return 'Person(%s,%s,%s,%s,%s)' % (self.name, self.birth_date, self.sex, self.height, self.weight)

    def __eq__(self, other):
        if type(other) == Person:
            return (self.name, self.birth_date, self.sex, self.height, self.weight) == (
                other.name, other.birth_date, other.sex, other.height, other.weight
            )
        elif type(other) == str:
            return self.__fuzzy_compare(other)
        else:
            return self.__repr__() == other.__repr__()

    def __fuzzy_compare(self, query):
        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]
            return max(rez)[0]

        def by_height(Q):
            q_height = max([int_val(q) for q in Q])
            if 'выше' in Q:
                return q_height < self.height
            if 'ниже' in Q:
                return q_height > self.height
            return q_height + 4 >= self.height >= q_height - 4

        def by_weight(Q):
            q_weight = max([int_val(q) for q in Q])
            if 'тяжелее' in Q:
                return q_weight < self.weight
            if 'легче' in Q:
                return q_weight > self.weight
            return q_weight + 2 >= self.weight >= q_weight - 2

        q_words = set(query.split())
        score = 0
        for m_words, method in zip([NAME_WORDS, HEIGHT_WORDS, WEIGHT_WORDS],
                                   [by_name, by_height, by_weight]):
            if m_words and q_words:
                score += method(q_words)

        return score > 0.49


evgeniy = Person('Евгений', '12.11.1982', 'мужской', 170, 72)
ivan = Person('Иван', '04.07.1992', 'мужской', 175, 67)
anna = Person('Анна', '16.10.1989', 'женский', 167, 48)
alena = Person('Алена', '26.03.1994', 'женский', 160, 51)

people = {
    evgeniy.key: evgeniy,
    ivan.key: ivan,
    anna.key: anna,
    alena.key: alena
}

queries = [
    'имя Евгений',
    'пол женский',
    'выше 170',
    'ниже 165',
    'легче 55',
    'тяжелее 70',
    'зовут Алена',
    'вес 67',
    'рост 175',
    'весит 72',
]

for query, person in product(queries, people.values()):
    if person == query:
        pprint((query, person))
