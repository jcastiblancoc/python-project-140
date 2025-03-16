# brain_games/games/even.py
import random

from brain_games.games.engine import play_game


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer


def play_even_or_odd(name):
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(name, rules, generate_question)