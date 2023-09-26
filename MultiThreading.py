import threading

from Task import init

# Create a specific thread amount that will run the print_numbers function
Thread_Amount = 10
threads = []

for i in range(Thread_Amount):
    thread = threading.Thread(target=init)
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for both threads to finish
for thread in threads:
    thread.join()

print ("Task Complete")