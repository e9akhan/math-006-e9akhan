"""
    Module Name :- solver
    Method(s) :- solver
"""

def solver(start, end, even=False, odd=False):
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

    for i in range(start, end+1):
        squares_sum += i**2

    sums_square = ((end*(end+1)/2)-(start*(start-1)/2))**2

    diff = sums_square - squares_sum
    return abs(diff)

if __name__ == '__main__':
    print(f'solver(1, 10) = {solver(1, 10)}')
