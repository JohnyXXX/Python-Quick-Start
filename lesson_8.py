from itertools import product
from pprint import pprint

from lesson_7_task_3_module import compare, int_val

ADDRESS_WORDS = {'дом', 'улица', 'живет', 'квартира'}
NAME_WORDS = {'имя', 'зовут', 'фамилия', 'отчество'}
AGE_WORDS = {'возраст', 'старше', 'младше'}


class Person:
    def __init__(self, last_name, first_name, middle_name, age, street, house, apartment):
        self.last_name, self.first_name, self.middle_name, self.age, self.street, self.house, self.apartment = last_name, first_name, middle_name, age, street, house, apartment
        self.key = (first_name, street)

    def __repr__(self):
        return "Person('%s','%s','%s',%s,'%s',%s,%s)" % (
            self.last_name, self.first_name, self.middle_name, self.age, self.street, self.house, self.apartment)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.last_name, self.first_name, self.middle_name, self.age, self.street, self.house,
                    self.apartment) == (
                       obj.last_name, obj.first_name, obj.middle_name, obj.age, obj.street, obj.house, obj.apartment)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    def __fuzzy_compare(self, query):
        def by_address(Q):
            Q = Q - ADDRESS_WORDS
            W = set(self.street.split() + str(self.house).split() + str(self.apartment).split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]
            return max(rez)[0]

        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.last_name.split() + self.first_name.split() + self.middle_name.split())
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


lena = Person("Иванова", "Лена", "Николаевна", 19, "Пушкина", 14, 115)
oleg = Person("Петров", "Олег", "Константинович", 34, "Ленскoго", 10, 11)
olga = Person("Бузова", "Ольга", "Игоревна", 28, "Онегина", 11, 12)
nata = Person("Ростова", "Наташа", "Павловна", 17, "Ростова", 16, 15)

queries = [
    'имя Ольга',
    'возраст 30',
    'старше 20',
    'отчество Константинович',
    'младше 20',
    'живет на Пушкина',
    'фамилия Бузова',
    'дом 10',
    'фамилия ростова',
    'зовут нташа',
    'фамилия петров',
    'квартира 115',
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
