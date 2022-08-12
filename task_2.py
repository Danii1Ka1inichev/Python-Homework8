from functools import reduce

sum = 0


def my_reduce(function, iterable, *index):
    if index:
        try:
            some_object_iterator = iter(index[0])
            return print(f'Ошибка: начальный индекс не может быть {type(index)}')
        except TypeError:
            initializer = index[0]
            print(initializer)
            sum = function(initializer, iterable[0])
            for i in range(len(iterable)):
                if i != 0:
                    print(f'sum({sum})+iterable[i]({iterable[i]})= {sum + iterable[i]}')
                    sum = function(sum, iterable[i])
    else:
        sum = function(iterable[0], iterable[1])
        initializer = 1
        if len(iterable) > 2:
            for i in range(len(iterable)):
                if i > initializer:
                    sum = function(sum, iterable[i])

    print(sum)


b = [8, 1, 2, 3, 4, 5]
c = [1, 2]
d = [1, 2, 3, 4]


my_reduce(lambda a, x: a * x, d, 4)

sum1 = reduce(lambda a, x: a * x, d, 4)
print(sum1)

