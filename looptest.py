import time

start_time = time.time()
count = 0

while True:
    print("Hello World")
    count += 1
    if time.time() - start_time >= 1.0:  # Check if, 1 second has passed
        break

print("Loops in a second:", count)
