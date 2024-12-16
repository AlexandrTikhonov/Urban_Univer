import multiprocessing as mp
import time


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    file_names = [f'./file {number}.txt' for number in range(1, 5)]

    # """ Линейный вызов """
    # start_time = time.time()
    # for file_name in file_names:
    #     read_info(file_name)
    # lin_time = time.time() - start_time
    # print(f'Линейный вызов: {lin_time: .6f} секунд')                # --> Линейный вызов:  10.118455 секунд

    """ Многопроцессорный вызов """
    start_time = time.time()
    with mp.Pool() as pool:
        pool.map(read_info, file_names)
    parallel_time = time.time() - start_time
    print(f'Многопроцессный вызов: {parallel_time: .6f} секунд')  # --> Многопроцессный вызов:  5.349248 секунд
