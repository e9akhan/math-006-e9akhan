"""
    Module Name :- solver
    Method(s) :- solver
"""


def solver(start, end):
    """
    Find the sum of square of numbers and square of sum of numbers
    over a range

    Args:
        start(int) :- Starting point of range.
        end(int) :- Ending point of range.

    Return:
        Absolute difference of sum of square of numbers and square of sum of
        numbers.
    """
    squares_sum = 0
    total = 0

    for i in range(start, end + 1):
        squares_sum += i**2
        total += i

    diff = (total**2) - squares_sum
    return abs(diff)


if __name__ == "__main__":
    print(f"solver(1, 10) = {solver(1, 10)}")
