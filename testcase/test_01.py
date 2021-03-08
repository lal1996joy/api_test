# from test_04 import max_version


def func(x):
    return x + 1


# @max_version
def test_answer():
    assert func(3) == 14
    print("打印信息")


def test_answer1():
    assert func(3) == 4
