from models.boss import Boss


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss = None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self._boss = boss
            boss.add_worker(self)

    def __repr__(self):
        return self.name
