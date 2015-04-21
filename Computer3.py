import RussianPeasantsAlgorithm
from collections import deque

CACHE = {}

last_five_questions = deque("", 5)

def print_name():
    return str(__name__)

def last_multiplied_handler():
    print list(last_five_questions)
    return list(last_five_questions)


def multiply_handler(x, y):
    key = [x,y]
    if key in CACHE:
        last_five_questions.appendleft([CACHE[key], key])
        return CACHE[key]

    answer = RussianPeasantsAlgorithm.russian_peasant_rec(x, y)
    last_five_questions.append([answer, key])
    CACHE[key] = answer
    return answer

