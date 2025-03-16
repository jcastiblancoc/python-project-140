# brain_games/scripts/brain_even.py
from brain_games.cli import welcome_user
from brain_games.games.even import play_even_or_odd


def main():
    name = welcome_user()
    play_even_or_odd(name)


if __name__ == "__main__":
    main()