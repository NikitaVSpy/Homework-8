import time
import psutil
import os


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def show_time(f):
    def wrapper_1(*args, **kwargs):
        launch = time.time()
        f(*args, **kwargs)
        finish = time.time()
        execution_func = finish - launch
        print('Время выполнения функции:', toFixed(execution_func, 4))

    return wrapper_1


def show_cpu(f):
    def wrapper_2(*args, **kwargs):
        launch = psutil.cpu_percent()
        f(*args, **kwargs)
        finish = psutil.cpu_percent()
        execution_func = finish - launch
        print('Загрузка ЦП:', execution_func, '%')

    return wrapper_2


def show_memory(f):
    def wrapper_3(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        launch = proc.memory_info().rss / 100000
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        finish = proc.memory_info().rss / 100000
        memory_usеd = finish - launch
        if memory_usеd < 0:
            memory_usеd = launch - finish
        print('Использованная память для выполнения функции:' + str(memory_usеd / 1000000), '\n')

    return wrapper_3


@show_memory
@show_cpu
@show_time
def list_elements(num):
    list_el = []
    for i in range(1, num + 1):
        list_el.append(i)
    return list_el


@show_memory
@show_cpu
@show_time
def list_elements_gen_seq(num):
    list_el_seq = [i for i in range(1, num + 1)]
    return list_el_seq


@show_memory
@show_cpu
@show_time
def list_elements_gen(num):
    for i in range(1, num + 1):
        yield i


N = 1000000
print('Создание списка посредством цикла:')
list_elements(N)

print('Создание списка с генератором последоватальностей:')
list_elements_gen_seq(N)

print('Создание списка с генератором:')
list_elements_gen(N)
