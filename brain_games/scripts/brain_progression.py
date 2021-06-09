# #!/usr/bin/python3

"""Description: brain progression game."""

from brain_games.engine import run
from brain_games.games import brain_progression


def main():
    """Run progression game."""
    run(brain_progression)


if __name__ == '__main__':
    main()
