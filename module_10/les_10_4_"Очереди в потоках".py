from queue import Queue
import time
import threading

def getter(queue):
    while True:                          # while not queue.empty: # условие что очередь не пуста(этот вариант не сработал)
        time.sleep(5)
        item = queue.get()
        print(threading.current_thread(), 'взял элемент', item)


q = Queue(maxsize=10)
thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил в очередь элемент', i)

