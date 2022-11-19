from math import sqrt, pow, hypot


def test_filter():
    assert list(filter(lambda x: x, [0, 1, 0, 1, 0, 1])) == [1,1,1]
    assert list(filter(lambda x: x > 0, range(-5, 5))) == [1,2,3,4]
    assert list(filter(lambda x: x, {0, 1, 0, 1, 0, 1})) == [1]

def test_map():
    #разные параметры в
    assert list(map(lambda x: x * x, range(3))) == [0, 1, 4]
    assert list(map(lambda x: x * x, range(6))) == [0, 1, 4, 9, 16, 25]
    assert list(map(lambda x: x * x, range(12, 1, -2))) == [144, 100, 64, 36, 16, 4]

    assert set(map(lambda x: x * x, range(3))) == {0, 1, 4}
    assert set(map(lambda x: x * x, range(6))) == {0, 1, 4, 9, 16, 25}
    assert set(map(lambda x: x * x, range(12, 1, -2))) == {144, 100, 64, 36, 16, 4}

    assert set(map(lambda x: x + 10, range(6))) == {10, 11, 12, 13, 14, 15}
    assert set(map(lambda x: x, range(6))) == {0, 1, 2, 3, 4, 5}
    assert set(map(lambda x: str(x), range(6))) == {'0', '1', '2', '3', '4', '5'}




def test_sorted():
    assert sorted([144, 100, 64, 36, 16, 4]) == [4, 16, 36, 64, 100, 144]
    assert sorted([0, 1, 4, 9, 16, 25], reverse = True) == [25, 16, 9, 4, 1, 0]
    assert sorted([(0,25), (1,16), (4,9), (9,4), (16,1), (25,0)]) == [(0,25), (1,16), (4,9), (9,4), (16,1), (25,0)]
    assert sorted([(0, 25), (1, 16), (4, 9), (9, 4), (16, 1), (25, 0)], key = lambda x: x[1]) == [(25, 0), (16, 1), (9, 4), (4, 9), (1, 16), (0, 25)]


def test_math_sqrt():
    assert sqrt(9) == 3
    assert sqrt(9) == 3.0
    assert sqrt(3) == 1.7320508075688772


def test_math_pow():
    # Return x**y (x to the power of y).
    assert pow(0.5, 0.5) == 0.7071067811865476
    assert pow(2, 2) == 4.0
    assert pow(2, 0.5) == 1.4142135623730951
    assert pow(0.5, 2) == 0.25

def test_math_hypot():
    # Return the Euclidean distance, sqrt(x*x + y*y).
    assert hypot(0, 0) == 0
    assert hypot(1, 0) == 1
    assert hypot(0, 1) == 1
    assert hypot(1, 1) == 1.4142135623730951