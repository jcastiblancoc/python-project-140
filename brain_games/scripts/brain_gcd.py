# brain_games/scripts/brain_gcd.py
from brain_games.cli import welcome_user
from brain_games.games.gcd import play_gcd


def main():
    name = welcome_user()
    play_gcd(name)


if __name__ == "__main__":
    main()