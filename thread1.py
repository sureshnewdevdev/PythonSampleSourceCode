import threading
import time

# 5
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
    m=10

# 10
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)
m=10
# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# print("Both threads have finished execution")

# print_numbers()
# print_letters()

# 15