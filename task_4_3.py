from timeit import timeit
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# сделаем вариант функции через list comprehensions

def revers_4(enter_num):
    return int(''.join([i for i in reversed(str(enter_num))]))

# дополнительно сделаем функцию через рекурсию

def revers_5(enter_num, str_num = ''):
    if enter_num == 0:
        return int(str_num)
    else:
        str_num += str(enter_num % 10)
        return revers_5(enter_num // 10, str_num)

num = 123456789123456789978965412331234569874213666



print(timeit("revers(num)", globals=globals(), number=10000))    #0.16256943699999998
print(timeit("revers_2(num)", globals=globals(), number=10000))  #0.10867438400000001
print(timeit("revers_3(num)", globals=globals(), number=10000))  #0.007269236999999984
print(timeit("revers_4(num)", globals=globals(), number=10000))  #0.03851864700000002
print(timeit("revers_5(num)", globals=globals(), number=10000))  #0.25307619200000003

"""
Замер четырех функций показал, что перевод числа в строковый тип с последующим reverse(разворотом)
строки в разы сокращают время выполнения кода по сравнению с алгебраичискими операциями над числом.
Лучшее время исполнения кода показала функция 3,вариант с list comprehensions показал результат работы чуть медленне
лидера, т.к. здесь тоже был перевод числа в строковый вид, но за счет использования цикла время получилось больше.
Далее по увеличению времени идут два варианта с алгебраическимим операциями над числом, которые показали примерно
одинаковый результат. И самое худщее время показала функция с рекурсией.
"""