# brain_games/games/even.py
import random


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer


def play_even_or_odd(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        number, correct_answer = generate_question()
        print(f"Question: {number}")

        answer = input("Your answer: ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")