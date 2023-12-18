"""
    Module Name :- answer
    Method(s) :- answer
"""

from solver import solver


def answer():
    """
    Find the difference of sum of squares of number and squares of sum
    of numbers between 1-100
    """
    return solver(1, 100)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
