import threading

counter = 0

# def increment(name):
#     """ Увеличивает счетчик на 1 """
#     global counter
#     for i in range(1000):
#         counter += 1
#         print(name, counter)
#
#
# def decrement(name):
#     """ Уменьшает счетчик на 1"""
#     global counter
#     for i in range(1000):
#         counter -= 1
#         print(name, counter)
#
#
# thread1 = threading.Thread(target=increment, args=('thread1',))
# thread2 = threading.Thread(target=decrement, args=('thread2',))
# thread3 = threading.Thread(target=increment, args=('thread3',))
# thread4 = threading.Thread(target=decrement, args=('thread4',))
#
# thread1.start()
# thread3.start()
# thread2.start()
# thread4.start()

### ----------- пример с замком (блокировка)
lock = threading.Lock()
print(lock.locked())


# def increment(name):
#     """ Увеличивает счетчик на 1 """
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         print(name, counter, lock.locked())
#     lock.release()
#
#
# def decrement(name):
#     """ Уменьшает счетчик на 1"""
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter -= 1
#         print(name, counter, lock.locked())
#     lock.release()
#
#
# thread1 = threading.Thread(target=increment, args=('thread1',))
# thread2 = threading.Thread(target=decrement, args=('thread2',))
# thread3 = threading.Thread(target=increment, args=('thread3',))
# thread4 = threading.Thread(target=decrement, args=('thread4',))
#
# thread1.start()
# thread3.start()
# thread2.start()
# thread4.start()

### ----- упрощаем код с помощью оператора with, который автоматически отключит блокировку после выполнения части кода
def increment(name):
    """ Увеличивает счетчик на 1 """
    global counter
    with lock:
        for i in range(1000):
            counter += 1
            print(name, counter, lock.locked())



def decrement(name):  # в этой части кода попробуем использовать блоки Try, Exception, finally для обработки исключений
    """ Уменьшает счетчик на 1"""
    global counter
    try:
        lock.acquire()
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())
    except Exception:
        pass
    finally:
        lock.release()



thread1 = threading.Thread(target=increment, args=('thread1',))
thread2 = threading.Thread(target=decrement, args=('thread2',))
thread3 = threading.Thread(target=increment, args=('thread3',))
thread4 = threading.Thread(target=decrement, args=('thread4',))

thread1.start()
thread3.start()
thread2.start()
thread4.start()