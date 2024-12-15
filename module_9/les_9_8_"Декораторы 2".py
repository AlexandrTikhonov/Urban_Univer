import time
import sys

def func_gen_dec(procision):
    def dec(func):
        def wrapper(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)

            ended_at = time.time()
            elapsed = round(ended_at - started_at, procision)
            print(f'Функция работала {elapsed} секунд(ы)')
            return result
        return wrapper
    return dec

@func_gen_dec(procision=6)
def digits(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))

sys.set_int_max_str_digits(10**5)

time_track_procision_6 = func_gen_dec(procision=2)
digits = time_track_procision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)