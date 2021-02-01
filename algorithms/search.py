def fibonacci_search(data: list, item: int) -> tuple:
    """
        Fibbonachi search implemntation.
        WORKS ONLY WITH sorted lists.
        Return tuple(position_in_list, iteration) if found, otherwise raise Exception
    """
    iteration = 1
    if not data:
        raise Exception('Empty data')

    if item > data[-1] or item < data[0]:
        raise Exception('Not found')

    def search(start_position=0, *, reverse=False):
        seq = _fibonacci_sequence_generator()
        nonlocal iteration
        while True:
            iteration += 1
            i = -next(seq) if reverse else next(seq)
            # if i > len(data):
            #     # print(f'Fib number {i}, step {iteration}, out of range')
            #     return search(reverse=True)
            # else:
            #     print(f'Fib number {i}, step {iteration}, element {data[start_position + i]}')

            if i > len(data):
                return search(reverse=True)
            elif item == data[start_position + i]:
                return (start_position + i, iteration)
            elif reverse and item > data[start_position + i]:
                return search(start_position + i)
            elif not reverse and item < data[start_position + i]:
                return search(start_position + i, reverse=True)

    return search()


def binary_search(data: list, item: int) -> tuple:
    """
        Binary search implemntation.
        WORKS ONLY WITH sorted lists.
        Return tuple(position_in_list, iteration) if found, otherwise raise Exception
    """
    iteration = 1
    if not data:
        raise Exception('Empty data')

    if item > data[-1] or item < data[0]:
        raise Exception('Not found')

    def search(start_position=0, end_postion=len(data)):
        nonlocal iteration
        iteration += 1
        middle = (end_postion + start_position) // 2
        if start_position < end_postion:
            if item == data[middle]:
                return (middle, iteration)
            elif item > data[middle]:
                return search(middle, end_postion)
            elif item < data[middle]:
                return search(0, middle)
        else:
            raise Exception('Not found')

    return search()


def _fibonacci_sequence_generator():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
