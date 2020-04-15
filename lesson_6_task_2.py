'''
Реализовать поиск по полям типа
рост больше 120
имя Наташа
'''


class PersonForDict:
    def __init__(self, name, birth_date, sex, height, weight):
        self.name, self.birth_date, self.sex, self.height, self.weight = name, birth_date, sex, height, weight
        self.key = (name, birth_date)

    def __repr__(self):
        return 'Person(%s,%s,%s,%s,%s)' % (self.name, self.birth_date, self.sex, self.height, self.weight)


evgeniy = PersonForDict('Евгений', '12.11.1982', 'мужской', 170, 72)
ivan = PersonForDict('Иван', '04.07.1992', 'мужской', 175, 67)
anna = PersonForDict('Анна', '16.10.1989', 'женский', 167, 48)
alena = PersonForDict('Алена', '26.03.1994', 'женский', 160, 51)

people = {
    evgeniy.key: evgeniy,
    ivan.key: ivan,
    anna.key: anna,
    alena.key: alena
}

height_query = input('Введите нижнюю границу роста: ')
name_query = input('Введите имя: ')

result_height = []
result_name = []

for person in people.values():
    if person.height >= int(height_query):
        result_height.append(person)
    if person.name.lower() == name_query.lower():
        result_name.append(person)

print(result_height)
print(result_name)
