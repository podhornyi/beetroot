import asyncio


class AsyncFib:

    def __init__(self, n: int = 100, prefix: str = ''):
        self._n = n
        self._prefix = prefix
        self._a, self._b = 0, 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._a > self._n:
            raise StopAsyncIteration
        current = self._a

        self._a, self._b = self._b, self._a + self._b
        await asyncio.sleep(0)
        return f'{self._prefix} {current}' if self._prefix else str(current)


async def iter_me(iterator):
    async for i in iterator:
        print(i)


async def gen(n = 100):
    a, b = 0, 1
    while n > a:
        yield a
        a, b = b, a + b
        await asyncio.sleep(0)



async def main():
    await asyncio.gather(
        iter_me(AsyncFib(100, 'A')),
        iter_me(AsyncFib(100, 'B')),
        iter_me(AsyncFib(100, 'C')),
        iter_me(gen(200))
    )


if __name__ == '__main__':
    asyncio.run(main())