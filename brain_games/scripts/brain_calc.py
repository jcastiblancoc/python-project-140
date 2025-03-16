# brain_games/scripts/brain_calc.py
from brain_games.cli import welcome_user
from brain_games.games.calc import play_calc


def main():
    name = welcome_user()
    play_calc(name)


if __name__ == "__main__":
    main()