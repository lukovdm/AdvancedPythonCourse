import RussianPeasantsAlgorithm
from collections import deque

CACHE = {}

last_five_questions = deque("", 5)

def print_name():
    return str(__name__)

def last_multiplied_handler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    pass


def multiply_handler(x, y):
    key = str(x)+"*"+str(y)
    if key in CACHE:
        last_five_questions.append([key, CACHE[key]])
        return CACHE[key]

    answer = RussianPeasantsAlgorithm.russian_peasant_rec(x, y)
    last_five_questions.append([key, answer])
    CACHE[key] = answer
    return answer

