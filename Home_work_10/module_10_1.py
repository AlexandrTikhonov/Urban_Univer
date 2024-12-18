import threading
import time


def write_words(word_count, file_name):
    with open(file_name,'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_first = time.time()
write_words(5, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_first = time.time()
time_first = end_first - start_first
print(f'Работа потоков: {time_first: .6f}') # --> Работа потоков:  33.566622

start_last = time.time()
threads = []

threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_last = time.time()
time_last = end_last - start_last
print(f'Работа потоков: {time_last: .6f}') # --> Работа потоков:  20.040313