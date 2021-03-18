from functools import reduce

a = set([5, 6, 3, 3, 9])
print(a)

b = frozenset([5, 6, 3, 3, 9])

c = {'ll': 1, 'kk': 9, 'ss': 8, 'll': 44}
for i in c.items():
    print(i)

sum = lambda x, y: x + y
print(sum(1, 2))


def info(func):
    print("函数名称：", func.__name__)
    print("函数描述：", func.__doc__)


# 装饰器
# @info
def add(x, y):
    """加法函数"""
    return x + y


# 高阶函数
info(add)

add1 = lambda x: x + 1  # 处理函数，由于一次处理一个，所有只能有一个参数
data = [1, 3, 5, 7, 9]
data1 = {1, 3, 5, 7, 9}
new_data = list(map(add1, data))  # map(add1,  data)  实际上是一个生成器，不会自动执行，必须遍历或者转成列表才会执行
print(new_data)

is_even = lambda x: x % 2 == 0  # 过滤函数，x是偶数是 x对2取模==0，返回True，奇数时不等于0，返回False。
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_data = list(filter(is_even, data))  # filter同样是一个生成器，需要转列表才会执行。
print(new_data)

add = lambda x, y: x + y
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = reduce(add, data)
print(sum)


def check(add):  # 外部函数，接受一个add函数

    def new_add(x, y):  # 内部函数
        if not isinstance(x, int) or not isinstance(y, int):  # 参数类型校验
            raise TypeError('x,y两个参数必须是整数类型')
        result = add(x, y)  # 可以使用外部函数参数add并得到结果
        # return result

    return new_add  # 返回替换后的new_add函数，具有函数add的功能，还加了参数检查功能


def add(x, y):
    return x + y


s = add(4, 5)
print(s)

def factorial(n):
    if n <= 1:  # 出口条件
        return 1
    else:
        return n * factorial(n - 1)  # 本层乘以n，然后递归调用自身处理下一层


print(factorial(4))

