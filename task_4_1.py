from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# реализуем эту же функцию через list comprehensions

def func_2(nums):
   return [i for i in range(len(nums)) if i % 2 == 0]

my_list = [i for i in range(100)]


print(timeit("func_1(my_list)", globals=globals(), number=1000))  # 0.014109743000000004
print(timeit("func_2(my_list)", globals=globals(), number=1000))  # 0.007253677

'''
Несмотря на то, что обе функции имеют линейную сложность O(n), замер времени выполнения кода показал, что 
list comprehenshions в два быстрее, чем перебор циклом с добавлением элемента, т.к. при итерации мы сначала создаем 
новый список, затем методом append(), добавляем в него элементы, что приводит к дополнительному расходу оперативной 
памяти. List comprehensions производит операции внутри итерации: он берет элемент из списка, сравнивает его с условием, 
и если элемент удовлетворяет условию,то оставляет его, в противном случае элемент пропускается.
'''

