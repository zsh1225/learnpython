
def fibs(num):
    """
    This is a Fibnacci function
    """
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result  # This is a comment

n=1
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)
knights = ['we', 'are', 'the', 'knights', 'who', 'we','say', 'ni']
knights.index('we')
knights.index('we', 5)
knights[4] # see the difference
