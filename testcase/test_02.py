import pytest


class TestDemo02:
    def func(self, x):
        return x + 1

    @pytest.mark.tag01
    def test_01(self):
        assert self.func(3) == 14

    def test_02(self):
        assert self.func(3) == 5

    @pytest.mark.tag02
    def test_03(self):
        assert self.func(3) == 4




