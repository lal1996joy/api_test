import pytest


def setup_module():
    print('\n====初始化模块====')


def teardown_module():
    print('\n====清除模块====')


class TestDemo01:
    def setup_class(self):
        print('\n====初始化类====')

    def teardown_class(self):
        print('\n====清除类====')

    def setup_method(self):
        print('\n====初始化方法====')

    def teardown_method(self):
        print('\n====清除方法====')

    def test_101(self):
        print("\n测试用例test_101执行")
        assert 1 == 1

    def test_102(self):
        print("\n测试用例test_102执行")
        assert 1 == 1

    def test_103(self):
        print("\n测试用例test_103执行")
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_03.py'])
