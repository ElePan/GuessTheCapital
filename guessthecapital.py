from __future__ import unicode_literals
from prompt_toolkit import PromptSession
import random

def load_data():
    with open("cities.txt", mode = 'r', encoding='utf-8') as f:
        content = f.readlines()
    return [x.strip() for x in content]

def create_dict():
    content = load_data()
    return {
        city.split(",")[0].strip(): city.split(",")[1].strip()
        for city in content
    }

def decorator(word):
    return word.casefold().strip()

def check_answer(answer, capital):
    is_correct = decorator(answer) == decorator(capital)
    points = 0
    if is_correct:
        print('Result:', is_correct)
        points = 10
    else:
        print('Result:', is_correct, 'the capital is', capital)
        points = 0
    return points

def prompt():
    session = PromptSession()
    city_dic = create_dict()
    asked = []
    question = 0
    points = 0
    answer = "init"
    while answer != "exit" and question in range(5):
        try:
            country, capital = random.choice(list(city_dic.items()))
            while f'{country}' in asked:
                country, capital = random.choice(list(city_dic.items()))
            asked.append( f'{country}')

            print('Which is the capital of', f'{country}','?')
            answer = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print('Answer:', answer)
            points = points + check_answer(answer, f'{capital}')
        question = question + 1
    print('Exit, your score is', points,'/50!')

if __name__ == '__main__':
    prompt()