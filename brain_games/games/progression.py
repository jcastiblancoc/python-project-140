# brain_games/games/progression.py
import random

from brain_games.games.engine import play_game


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer


def play_progression(name):
    rules = 'What number is missing in the progression?'
    play_game(name, rules, generate_progression)