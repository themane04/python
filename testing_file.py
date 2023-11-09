import threading


def append_ok_indefinitely(i):
    print(f"Thread {i}")
    a = []
    while True:
        a.append("ok")


threads = list()
# Create a thread that runs the append_ok_indefinitely function
for i in range(8):
    thread = threading.Thread(target=append_ok_indefinitely, args=(i, ))
    threads.append(thread)
# Start the thread
for i in threads:
    i.start()
