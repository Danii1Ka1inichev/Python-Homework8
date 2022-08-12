
def my_map(function, iterable, *iterables):
    try:
        some_object_iterator = iter(iterable)
        [my_map(function, iterable[i]) for i in range(len(iterable))]
    except TypeError:
        function(iterable)
    except RecursionError:
        function(iterable)

    if iterables:
        try:
            some_object_iterator = iter(iterables)
            [my_map(function, iterables[i]) for i in range(len(iterables))]
        except TypeError:
            function(iterables)
        except RecursionError:
            function(iterables)


my_map(lambda x: print(x+1), [1, 2, 3, [4, 5]], 6, 7, [8, 9])
my_map(lambda x: print(x*2), 'hello', ['w', 'o', 'r'], 'l', 'd', '!')
