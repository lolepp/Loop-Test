import time
import random

start_time = time.time()
count = 0

# Check, if 1 second has passed
while True:
    number = random.randint(0, 10**100)
    print(number)
    count += 1
    if time.time() - start_time >= 10.0:
        break

print(f"Loops in a second: {count}\nAverage per second: {count/10}")
