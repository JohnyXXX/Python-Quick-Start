"""
В терминах ООП описать предметную область,
которую вы ранее описали словарем
"""


class Human:
    def __init__(self, fullname, birth_date, sex, height, weight):
        self.fullname = fullname
        self.birth_date = birth_date
        self.sex = sex
        self.height = height
        self.weight = weight


class Nutrition(Human):
    def eat(self, add_weight):
        self.weight += add_weight

    def starve(self, reduce_weight):
        self.weight -= reduce_weight
