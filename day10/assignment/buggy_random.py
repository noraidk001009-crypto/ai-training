import random
print(random.randint(1, 6))

#原先：print(random.randint(1, 6, 7))，原因：randint()函数需要两个参数，而这里给了三个参数。