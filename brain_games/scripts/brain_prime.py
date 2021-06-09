#!/usr/bin/python3

"""Description: brain prime game."""

from brain_games.engine import run
from brain_games.games import brain_prime


def main():
    """Run prime game."""
    run(brain_prime)


if __name__ == '__main__':
    main()
