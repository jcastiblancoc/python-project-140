# brain_games/scripts/brain_prime.py
from brain_games.cli import welcome_user
from brain_games.games.prime import play_prime


def main():
    name = welcome_user()
    play_prime(name)


if __name__ == "__main__":
    main()