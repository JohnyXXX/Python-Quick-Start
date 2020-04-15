# 1) Описать классом(ами) ваши данные


class PersonList:
    def __init__(self, name, birth_date, sex, height, weight):
        self.name, self.birth_date, self.sex, self.height, self.weight = name, birth_date, sex, height, weight

    def __repr__(self):
        return 'Person(%s,%s,%s,%s,%s)' % (self.name, self.birth_date, self.sex, self.height, self.weight)


evgeniy = PersonList('Евгений', '12.11.1982', 'мужской', 170, 72)
ivan = PersonList('Иван', '04.07.1992', 'мужской', 175, 67)
anna = PersonList('Анна', '16.10.1989', 'женский', 167, 48)
alena = PersonList('Алена', '26.03.1994', 'женский', 160, 51)

people = [
    evgeniy, ivan, anna, alena
]

print(people)
print(people[2])


class PersonDict:
    def __init__(self, name, birth_date, sex, height, weight):
        self.name, self.birth_date, self.sex, self.height, self.weight = name, birth_date, sex, height, weight
        self.key = (name, birth_date)

    def __repr__(self):
        return 'Person(%s,%s,%s,%s,%s)' % (self.name, self.birth_date, self.sex, self.height, self.weight)


evgeniy = PersonDict('Евгений', '12.11.1982', 'мужской', 170, 72)
ivan = PersonDict('Иван', '04.07.1992', 'мужской', 175, 67)
anna = PersonDict('Анна', '16.10.1989', 'женский', 167, 48)
alena = PersonDict('Алена', '26.03.1994', 'женский', 160, 51)

people = {
    evgeniy.key: evgeniy,
    ivan.key: ivan,
    anna.key: anna,
    alena.key: alena
}

print(people)
print(people[anna.key])
