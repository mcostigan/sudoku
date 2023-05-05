# Sudoku
[Sudoku](https://en.wikipedia.org/wiki/Sudoku) is a puzzle in which the player attempts to build a solution that does not violate any of the constraints:
1. Every row has numbers 1-9
2. Every column has numbers 1-9
3. All 9 3x3 boxes have numbers 1-9

# Linear Programming
[Linear Programming](https://en.wikipedia.org/wiki/Linear_programming) (LP) is an optimization technique where an objective function is maximized or minimized given a series of constraints, so long as the function and all of the constraints are linear equations

Integer LP is a type of LP where some subset of the solutions must be integers. This is NP-complete, while vanilla LP is polynomial. For Sudoku, the constraints are rigid and there is no true objective function, so integer LP reliably and quickly finds a solution

# Example
## Variables
Every row-column-number combination is a variable: 729 in total
## Constraints
The constraints described above can be easily converted into linear equations, i.e. the sum of all columns given a fixed number and row value is equal to 1.
## Objective Function
This is not necessary, since any solution will do. Though, if more than one solution exists and certain patterns were more desirable to you than others (or you wanted to promote randomness), you could specify one.
## Solve
I used [Google's OR Tools](https://developers.google.com/optimization/mip/mip_example) to solve the Integer LP problem. 

The `solver` outputs a grid representing a valid solution give your inputs:
```angular2html
5 6 8 2 4 7 1 3 9
3 4 2 1 9 5 8 7 6
1 9 7 8 6 3 5 4 2
9 2 6 7 8 1 4 5 3
8 5 1 4 3 9 2 6 7
4 7 3 5 2 6 9 1 8
6 8 5 3 1 2 7 9 4
7 3 4 9 5 8 6 2 1
2 1 9 6 7 4 3 8 5
```

# Run
Run `main.py` and give your puzzle input one cell at a time. When you are complete, type `#DONE` to call the `solver`.