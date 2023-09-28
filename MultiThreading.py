import threading

#from Task import init

def initThreads(ThreadAmount, task):
    # Create a specific thread amount that will run the print_numbers function
    threads = []
    for i in range(ThreadAmount):
        thread = threading.Thread(target=task)
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for both threads to finish
    for thread in threads:
        thread.join()

    print ("Task Complete")

