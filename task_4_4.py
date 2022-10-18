from timeit import timeit
from random import randint

array = []
for i in range(10000):
    array.append(randint(1, 100))


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Создадим функцию без метода count

def func_3():
    new_arrey = sorted(array)
    num = new_arrey[0]
    count = 0
    max_count = 0
    num_res = None
    for i in new_arrey:
        if i == num:
            count += 1
            if count > max_count:
                max_count = count
                num_res = i
        else:
            num = i
            count = 1
    return f'Чаще всего встречается число {num_res}, ' \
           f'оно появилось в массиве {max_count} раз(а)'

# Решение в одну строку

def func_4():
    return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
           f'оно появилось в массиве {array.count(max(array, key=array.count))} раз(а)'


print(func_1())   #Чаще всего встречается число 5, оно появилось в массиве 127 раз(а)
print(func_2())   #Чаще всего встречается число 5, оно появилось в массиве 127 раз(а)
print(func_3())   #Чаще всего встречается число 5, оно появилось в массиве 127 раз(а)
print(func_4())   #Чаще всего встречается число 5, оно появилось в массиве 127 раз(а)

print(timeit("func_1", globals=globals(), number=10000))     #0.000237374999999318
print(timeit("func_2", globals=globals(), number=10000))     #0.00024333400000031702
print(timeit("func_3", globals=globals(), number=10000))     #0.00026485299999912115
print(timeit("func_4", globals=globals(), number=10000))     #0.00023638200000064558

"""
По моим расчетам первые две функции должны работать медленнее, т.к. в цикле со сложностью O(n) присутствует метод
count, который усложняет функцию до квадратичной сложности. Третья и четвертая функции имеют линейную сложность и
по идее они должны работать быстрее, но по факту получилось, что все функции работатю примерно одинаково. Даже 
усложнение массива не изменило ситуацию. С точки зрения синтаксиса четвертая функция самая лаконичная.
"""