#!/usr/bin/python3

"""Description: brain games - Brain calc game."""

from brain_games.engine import run
from brain_games.games import brain_calc


def main():
    """Run calculate game."""
    run(brain_calc)


if __name__ == '__main__':
    main()
