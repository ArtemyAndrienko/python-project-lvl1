#!/usr/bin/python3

"""Description: brain gcd game."""

from brain_games.engine import run
from brain_games.games import brain_gcd


def main():
    """Run gcd game."""
    run(brain_gcd)


if __name__ == '__main__':
    main()
