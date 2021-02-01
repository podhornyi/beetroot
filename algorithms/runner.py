from algorithms import fibonacci_search, binary_search


def run():
    _range = 0, 500, 2
    data = list(range(*_range))

    fibonacci_res = []
    binary_res = []

    start_lookup = -1000
    end_lookup = 1000

    for i in range(start_lookup, end_lookup):
        try:
            fibonacci_res.append(fibonacci_search(data, i))
        except Exception:
            pass
        try:
            binary_res.append(binary_search(data, i))
        except Exception:
            pass

    fib_wins = 0
    bin_wins = 0
    for i, item in enumerate(fibonacci_res):
        if item[1] <= binary_res[i][1]:
            fib_wins += 1
        else:
            bin_wins += 1

    print(f'searching in range({_range}) all numbers in range({start_lookup}, {end_lookup})')
    print(f'data len is {len(data)}')
    print(f'fib_wins: {fib_wins}, found {len(fibonacci_res)}')
    print(f'bin_wins: {bin_wins}, found {len(binary_res)}')
