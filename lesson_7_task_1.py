'''
Добавить вывод неподходящих
запросов и отладки
'''

from itertools import product
from pprint import pprint

from lesson_7_task_1_module import compare, int_val

ADDRESS_WORDS = {'дом', 'улица', 'живет'}
NAME_WORDS = {'имя', 'зовут', 'фамилия'}
AGE_WORDS = {'возраст', 'старше', 'младше'}


class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)

    def __repr__(self):
        return "Person('%s',%s,'%s')" % (self.name, self.age, self.address)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.name, self.age, self.address) == (obj.name, obj.age, obj.address)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    def __fuzzy_compare(self, query):
        def by_address(Q):
            Q = Q - ADDRESS_WORDS
            W = set(self.address.replace(',', '').split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]
            return max(rez)[0]

        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]

            return max(rez)[0]

        def by_age(Q):
            query_age = max([int_val(q) for q in Q])
            if 'старше' in Q:
                return query_age < self.age
            if 'младше' in Q:
                return query_age > self.age
            return query_age + 5 >= self.age >= query_age - 5

        q_words = set(query.split())
        score = 0
        for m_words, method in zip([ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
                                   [by_address, by_name, by_age]):
            if m_words & q_words:
                score += method(q_words)

        return score > 0.49


lena = Person("Лена", 19, "Пушкина,  14, 115")
oleg = Person("Олег", 34, "Ленскoго, 10,  11")
olga = Person("Ольга", 28, "Онегина,  11,  12")
nata = Person("Наташа", 17, "Ростова,  16,  15")

queries = [
    'имя Ольга',
    'возраст 30',
    'старше 20',
    'младше 20',
    'живет на Пушкина',
    'дом 10',
    'фамилия ростова',
    'зовут нташа',
]

people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
}

for query, person in product(queries, people.values()):
    if person == query:
        pprint((query, person))

for query, person in product(queries, people.values()):
    print(f'{person} = {query}', person == query)
    if person != query:
        pprint((query, person))
