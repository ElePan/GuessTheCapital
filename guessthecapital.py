from __future__ import unicode_literals

import random
from prompt_toolkit import PromptSession


def load_data():
    with open('cities.txt', mode='r', encoding='utf-8') as f:
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


def questionner(city_dic):
    cities_registry = []
    city_dic = city_dic

    def generate_question():
        return random.choice(list(city_dic.items()))

    def launch_question():
        country, capital = generate_question()
        # This will never happen but it is exit condition
        if len(cities_registry) >= len(city_dic.keys()):
            return 0
        if country not in cities_registry:
            cities_registry.append(country)
            return country, capital
        else:
            return launch_question()

    return launch_question


def capital_prompt():
    session = PromptSession()
    city_dic = create_dict()
    question = 0
    points = 0
    answer = "init"
    launcher_question = questionner(city_dic)
    print("Write exit or press Ctrl+d to exit")
    while answer != "exit" and question in range(5):
        try:
            country, capital = launcher_question()
            print(f'Which is the capital of {country} ?')
            answer = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print('Answer:', answer)
            points = points + check_answer(answer, f'{capital}')
        question = question + 1
    print(f'Exit, your score is {points}/50!')


if __name__ == '__main__':
    capital_prompt()
