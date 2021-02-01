from contextlib import contextmanager
with open('../requirements.txt') as f:
    print(f.readlines())


class FileOpener:

    def __init__(self, file_name, access_method='r'):
        self.file_name = file_name
        self.access_method = access_method

    def __enter__(self):
        print('Entering')
        self._file = open(self.file_name, self.access_method)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting', exc_type, exc_val, exc_tb)
        self._file.close()


# with FileOpener('requirements.txt') as f:
#     print(f.readlines())
#     raise ValueError('Test value error')


@contextmanager
def file_opener(file_name, access_method='r'):
    file = None
    try:
        file = open(file_name, access_method)
        yield file
    except Exception as e:
        pass
    finally:
        print('FINALLY')
        if file:
            file.close()


with file_opener('../requirements.txt') as f:
    print(f.readlines())


def sequence_ensurance():
    print(1)
    yield
    print(2)
    yield
    print(3)
    yield
    print(4)

for _ in sequence_ensurance():
    pass