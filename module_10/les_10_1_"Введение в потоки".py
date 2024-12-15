import threading
import time

def func_1():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())


def func_2(x):
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())
        print(threading.current_thread().is_alive())

thread = threading.Thread(target=func_2, args=(1,), daemon=True)
thread.start()
# thread.join() # этой командой мы приостановили основной поток
print(thread.is_alive())
func_1()

print(threading.enumerate())
print(threading.current_thread())