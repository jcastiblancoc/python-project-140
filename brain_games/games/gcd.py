# brain_games/games/gcd.py
import random
from math import gcd

from brain_games.games.engine import play_game


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def play_gcd(name):
    rules = 'Find the greatest common divisor of given numbers.'
    play_game(name, rules, generate_question)