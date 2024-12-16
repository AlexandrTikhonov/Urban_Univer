from threading import Thread
import time
from queue import Queue
from random import randint


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        time_random = randint(3, 10)
        time.sleep(time_random)


class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f'{next_guest.name} вышел из очереди и сел(-а) за стол номер {table.number}')


if __name__ == '__main__':
    cafe = Cafe(Table(1), Table(2), Table(3))

    guests = [Guest('Vasya'), Guest('Petya'), Guest('Masha'), Guest('Sasha'), Guest('Dasha')]

    cafe.guest_arrival(*guests)
    cafe.discuss_guests()
