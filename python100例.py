# https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650372551&idx=1&sn=cd4e2ad70524a804f91cec5f20c6fdf7&chksm=be9cc29389eb4b85172c0ef791385f8744922bad9f256967d53fe52e2937bacd4b5f831fd5db&mpshare=1&scene=1&srcid=&sharer_sharetime=1592600327291&sharer_shareid=207ab7f15ce008ca518497bc45b5f3cc&exportkey=Aa1nS5SIMfEvz9Kqb7T%2FqPA%3D&pass_ticket=rAphdP9dvA6lDjBdGE2ff%2BJHh%2BaCgmH59WzFvaddQxiSKZtmBnur2ks%2FZR5MCEMx&wx_header=0#rd
# 10进制转2进制
print(bin(10))
# 10进制转8进制
print(oct(10))
# 十进制转换为十六进制：
print(hex(10))
# ASCII字符对应的十进制数
print(ord('A'))
# zip
a = [1, 2, 3]
b = ['a','b','c']
c=dict(zip(a,b))
print(c)
# 格式化字符串常见用法

# >>> print("i am {0},age {1}".format("tom",18))
# i am tom,age 18
# >>> print("{:.2f}".format(3.1415926)) # 保留小数点后两位
# 3.14
# >>> print("{:+.2f}".format(-1)) # 带符号保留小数点后两位
# -1.00
# >>> print("{:.0f}".format(2.718)) # 不带小数位
# 3
# >>> print("{:0>3d}".format(5)) # 整数补零，填充左边, 宽度为3
# 005
# >>> print("{:,}".format(10241024)) # 以逗号分隔的数字格式
# 10,241,024
# >>> print("{:.2%}".format(0.718)) # 百分比格式
# 71.80%
# >>> print("{:.2e}".format(10241024)) # 指数记法
# 1.02e+07
class C(object):
    def __init__(self):
        self._x = None
 
    def getx(self):
        return self._x
 
    def setx(self, value):
        self._x = value
 
    def delx(self):
        del self._x
 
    x = property(getx, setx, delx, "I'm the 'x' property.")
c = C()
# c.x = 10
help(c)
print(c)