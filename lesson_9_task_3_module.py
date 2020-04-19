import re
from itertools import product
from random import randint

NOT_FOUND = '$'
MIN_WORD_SIMILARITY = 0
MIN_QUESTION_SIMILARITY = 0.5


class Head():
    storage = dict()
    answers = ('да', 'нет')

    def compare(self, s1, s2):
        count = 0
        for ngram in (s1[i:i + 3] for i in range(len(s1) - 1)):
            count += s2.count(ngram)
        return count / max(len(s1), len(s2))

    def think(self, question):
        words = tuple(re.sub(r'[!?.,;:-]', ' ', question).split())
        # print(words)
        try:
            return "Был ответ %s" % self.storage[words]
        except KeyError:
            try:
                answer = NOT_FOUND
                for key in self.storage:
                    rez = []
                    for w1, w2 in product(key, words):
                        w = self.compare(w1, w2)
                        # print(w)
                        if w > MIN_WORD_SIMILARITY:
                            rez += [(w, w1, w2)]
                            # print(rez)
                    if sum((x[0] for x in rez)) / len(rez) > MIN_QUESTION_SIMILARITY:
                        # print(sum((x[0] for x in rez)) / len(rez))
                        answer = self.storage[key]
                assert answer != NOT_FOUND
                return "Кажется был ответ: %s" % answer
            except (AssertionError, ZeroDivisionError):
                answer = self.answers[randint(0, len(self.answers) - 1)]
                self.storage.update({words: answer})
                return "Ответ: %s" % answer


if __name__ == '__main__':
    head = Head()
    print(head.think('Какой-то вопрос?'))
    print(head.think('Какой-то вопрос?'))
    print(head.think('Какой то вопросик?'))
    print(head.think('Какой то вопросчек?'))
    print(head.think('Какой то вопросчечечек?'))
    print(head.think('Сегодня будет дождь?'))
    print(head.think('Завтра будет дождь?'))
