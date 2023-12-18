import solver


def test_solver():
    assert solver.solver(start=15812, end=91581312, even=False, odd=True) == 82775742
