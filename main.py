from typing import Set, Tuple

import solver


def _get_starting_positions() -> Set[Tuple[int, int, int]]:
    starting_positions: Set[Tuple[int, int, int]] = set()

    while True:
        user_input = input("Enter a position (row, column, number) or #DONE:")
        if user_input.startswith("#DONE"):
            return starting_positions

        row, col, number = tuple(int(value.strip()) for value in user_input.split(","))
        assert -1 < row < 9
        assert -1 < col < 9
        assert 0 < number, 9

        starting_positions.add((row, col, number))


if __name__ == '__main__':
    starting_positions = _get_starting_positions()
    solver.solve(starting_positions)
