import sys
import pytest
if 2 > 1:
    pytest.skip("跳过整个模块", allow_module_level=True)


# max_version = pytest.mark.skipif(sys.version_info > (3, 6), reason='python版本大于3.6就跳过')

# @max_version
# pytestmark = pytest.mark.skipif(sys.version_info > (3, 6), reason='python版本大于3.6就跳过')


class TestDemo01:

    # @pytest.mark.skip(reason='我要跳过')
    # @pytest.mark.skipif(sys.version_info > (3, 6), reason='python版本大于3.6就跳过')
    # @max_version
    def test_01(self):
        print('\ntest_01方法执行')
        assert 1 == 1

    def test_02(self):
        # if 2 > 1:
        #     pytest.skip("2>1才跳过")
        print('\ntest_02方法执行')
        assert 1 == 1

    def test_03(self):
        print('\ntest_03方法执行')
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_04.py'])
