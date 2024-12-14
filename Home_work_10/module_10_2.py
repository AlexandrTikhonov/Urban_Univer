import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 0
        elements = 100
        while elements > 0:
            counter += 1
            time.sleep(1)
            elements = elements - self.power
            if elements < 0:
                elements = 0
            print(f'{self.name} сражается {counter}-й день ..., осталось {elements} воинов.')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')


threads = []

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight('Sir Galahad', 20)
second_knight.start()

threads.append(first_knight)
threads.append(second_knight)

for thread in threads:
    thread.join()
print(f'\nВсе битвы закончились')
