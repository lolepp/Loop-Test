import time

start_time = time.time()
count = 0

while True:
    print("Hello World")
    count += 1
    if time.time() - start_time >= 1.0:  # Überprüfen Sie, ob 1 Sekunde vergangen ist
        break

print("Schleifendurchläufe pro Sekunde:", count)
