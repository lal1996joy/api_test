
import pytest


if __name__ == '__main__':
    # 通过文件执行测试
    # -s:在运行测试脚本时，为了调试或打印一些内容，我们会在代码中加一些print内容，但是在运行pytest时，这些内容不会显示出来。如果带上-s，就可以显示了
    pytest.main(['-s', 'test_01.py'])


    # pytest ‐x  # 第一次测试失败后停止测试
    # pytest ‐‐maxfail = 2  # 第2次测试失败后停止测试
    # pytest.main(['-x', 'test_01.py'])


    # 通过文件夹执行测试
    # pytest.main(['testcase'])


    # 通过关键字表达式来进行测试 -k
    # 这种方式会执行文件名，类名以及函数名与给定的字符串表达式相匹配的测试用例。
    # 会执行TestDemo02.test_02但是不会执行TestDemo02.test_01
    # pytest.main(['-k', 'Demo02 and not 01'])


    # 通过节点 id 来进行测试
    # 参数化的类名、函数名和参数，用::分隔。
    # 可以通过下面的方式运行模块中的指定的测试用例,从结果看出，执行了test_02.py内TestDemo02类下的test_01方法
    # pytest.main(['testcase/test_02.py::TestDemo02::test_01'])


    # 通过标记来执行 -m
    # 这种方式会运行所有通过装饰器 @pytest.mark.tag进行装饰的测试用例，所以我们来修改test_02.py文件
    # pytest.main(['-m', 'tag01 or tag02'])
