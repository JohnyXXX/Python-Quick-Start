"""
Сделать такой инт что 2 + 2 = 5
"""


class Var(int):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __add__(self, other):
        if self.value == 2 and other == 2:
            return self.value + other + 1
        else:
            return self.value + other


x = Var(2)
y = Var(2)

print(x + y)
