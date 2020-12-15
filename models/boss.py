from datetime import datetime


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__created_at = datetime.utcnow()
        self._workers = []

    def add_worker(self, worker: 'Worker'):
        if worker:
            self._workers.append(worker)

    @property
    def workers(self):
        return self._workers

    def __str__(self):
        return self.name

    def test(self):
        data = input("DATA:")
        return int(data)