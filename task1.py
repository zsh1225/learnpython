# def fibs(num):
#     """
#     This is a Fibnacci function
#     """
#     result = [0, 1]
#     for i in range(num-2):
#         result.append(result[-2] + result[-1])
#     return result  # This is a comment

# n=1
# x = y = [1, 2, 3]
# z = [1, 2, 3]
# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z)
# knights = ['we', 'are', 'the', 'knights', 'who', 'we','say', 'ni']
# knights.index('we')
# knights.index('we', 5)
# knights[4] # see the difference
a_list=[1,2,3,4,5]
b_list=a_list[:]
del a_list[0]
del a_list
print(b_list)
class demo:
    def __init__(self,num) -> None:
        self.num=num
def test(a,b):
    a.num,b.num=b.num,a.num
a=demo(1)
b=demo(2)
test(a,b)
print(a.num,b.num)