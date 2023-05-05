from typing import Set, Tuple

from ortools.linear_solver import pywraplp


def solve(starting_positions: Set[Tuple[int, int, int]]):
    solver = pywraplp.Solver.CreateSolver('SAT')
    variables = {}

    """
    VARIABLES:
    9^3 indicator variables: (row, col, number):= 1 if sudoku[row][col] == number else 0
    """
    for r in range(9):
        for c in range(9):
            for n in range(1, 10):
                variables[(r, c, n)] = solver.IntVar(0, 1, f"{r},{c},{n}")

    """
    CONSTRAINTS
    """
    # 1. The variables present in starting positions must be 1
    for position in starting_positions:
        solver.Add(variables[position] == 1)

    # 2. Each cell must have exactly one value
    for r in range(9):
        for c in range(9):
            solver.Add(sum([variables[(r, c, n)] for n in range(1, 10)]) == 1)

    # 3. Each row-number combination must show up exactly once
    for r in range(9):
        for n in range(1, 10):
            solver.Add(sum([variables[(r, c, n)] for c in range(9)]) == 1)

    # 4. Each col-number combination must show up exactly once
    for c in range(9):
        for n in range(1, 10):
            solver.Add(sum([variables[(r, c, n)] for r in range(9)]) == 1)

    # 5. Each box-number combination must show up exactly once
    for box_row in range(3):
        for box_col in range(3):
            for n in range(1, 10):
                solver.Add(sum([variables[r, c, num] for r, c, num in variables if
                                r // 3 == box_row and c // 3 == box_col and num == n]) == 1)

    """
    OBJECTIVE FUNCTION
    This doesn't actually matter. We are interested in any variable assignment that meets all of these conditions
    Any properly designed sudoku will have a distinct solution
    """
    solver.Maximize(0)

    """"
    SOLVE
    """
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        display = [['_' for _ in range(9)] for _ in range(9)]
        for row, c, num in variables:
            value = variables[row, c, num].solution_value()
            if value == 1:
                display[row][c] = str(num)
        print('\n'.join([' '.join(r) for r in display]))
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    example_positions = {
        (2, 0, 1),
        (6, 0, 6),
        (2, 1, 9),
        (4, 1, 5),
        (7, 1, 3),
        (2, 2, 7),
        (6, 2, 5),
        (8, 2, 9),
        (0, 3, 2),
        (1, 3, 1),
        (7, 3, 9),
        (0, 4, 4),
        (8, 4, 7),
        (0, 5, 7),
        (2, 5, 3),
        (3, 5, 1),
        (7, 5, 8),
        (2, 6, 5),
        (5, 6, 9),
        (8, 6, 3),
        (1, 7, 7),
        (4, 7, 6),
        (3, 8, 3),
        (5, 8, 8),
        (6, 8, 4)
    }
    solve(example_positions)
