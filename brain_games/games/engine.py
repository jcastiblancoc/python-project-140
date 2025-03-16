# brain_games/games/engine.py
def play_game(name, rules, generate_question):
    print(rules)

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        answer = input("Your answer: ").strip()

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