# brain_games/games/calc.py
import random

from brain_games.games.engine import play_game


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2

    return question, str(correct_answer)


def play_calc(name):
    rules = 'What is the result of the expression?'
    play_game(name, rules, generate_question)