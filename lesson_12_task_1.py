"""
В терминах ООП описать предметную область,
которую вы ранее описали словарем
"""


class Weight:
    def __init__(self, weight):
        self.weight = weight

    def eat(self, add_weight):
        self.weight += add_weight

    def starve(self, reduce_weight):
        self.weight -= reduce_weight


class Human(Weight):
    def __init__(self, fullname, birth_date, sex, height, weight):
        self.fullname = fullname
        self.birth_date = birth_date
        self.sex = sex
        self.height = height
        super().__init__(weight)

    def __str__(self):
        return f'Person({self.fullname}, {self.birth_date}, {self.sex}, {self.height}, {self.weight})'

# ivan = Human('Иванов Иван Иванович', '01.01.1999', 'мужской', 167, 74)
