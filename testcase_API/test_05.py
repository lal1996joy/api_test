import pytest


# 一个参数
@pytest.mark.parametrize("arg_1", [1, 2])
def test_01(arg_1):
    assert 1 == arg_1


# 多个参数
# values = [
#     (1, 1, 2),
#     (1, 2, 4),
#     (1, 3, 4)
# ]
#
#
# @pytest.mark.parametrize("a,b,c", values)
# def test_add(a, b, c):
#     assert (a + b) == c


if __name__ == '__main__':
    pytest.main(['-s', 'test_05.py'])
