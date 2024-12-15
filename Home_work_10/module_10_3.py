import threading
import time
from random import randint


lock = threading.Lock()

class Bank:

    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock


    def deposit(self):
        for i in range(100):
            random_num = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_num
            print(f'{i+1}. Пополнение: {random_num}. Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            random_num = randint(50, 500)
            print(f'{i+1}. Запрос на {random_num}')
            if random_num <= self.balance:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')


bk = Bank(0, lock)

th1 = threading.Thread(target=bk.deposit(), args=(bk,))
th2 = threading.Thread(target=bk.take(), args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')