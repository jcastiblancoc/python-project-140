# brain_games/scripts/brain_progression.py
from brain_games.cli import welcome_user
from brain_games.games.progression import play_progression


def main():
    name = welcome_user()
    play_progression(name)


if __name__ == "__main__":
    main()