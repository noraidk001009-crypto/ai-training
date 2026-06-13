total = 0
for i in range(1, 5):  # BUG: should sum 1..10
    total = total + i
print("Sum 1..10 should be 55:", total)
