print("Start")
total = 0
for i in range(1, 11):
    total = total + i

import random
rolls = [random.randint(1, 6) for _ in range(10)]
total_rolls = sum(rolls)

print("handle:", total_rolls, total)
print("Done")




