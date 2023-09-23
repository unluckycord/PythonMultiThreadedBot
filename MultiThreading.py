import threading

from Task import print_numbers

# Create a specific thread amount that will run the print_numbers function

threads = []

for i in range(10):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for both threads to finish
for thread in threads:
    thread.join()

print ("Task Complete")