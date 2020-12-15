import unittest

from models import Boss, Worker


class TestBoss(unittest.TestCase):

    def setUp(self):
        self.boss = Boss(1, 'Kola', 'Noname')

    def tearDown(self):
        pass

    def test_boss_workers_init(self):
        self.assertEqual(len(self.boss.workers), 0)

    def test_boss_workers_appending(self):
        self.assertEqual(0, len(self.boss.workers))
        self.boss.add_worker(Worker(1, 'Petro', ''))
        self.boss.add_worker(None)
        self.boss.add_worker(Worker(1, 'Petro', ''))
        self.assertEqual(2, len(self.boss.workers))

    def test_boss_workers_capacity(self):
        self.assertTrue(len(self.boss.workers) == 0)
        self.boss.add_worker(Worker(1, 'Petro', ''))
        self.assertTrue(len(self.boss.workers) > 0)

    def test_boss_workers_sequence(self):
        worker1 = Worker(1, 'w1', '')
        worker2 = Worker(1, 'w2', '')
        worker3 = Worker(1, 'w3', '')

        _workers = [worker1, worker3, worker2]

        for worker in _workers:
            self.boss.add_worker(worker)

        self.assertTrue(self.boss.workers == _workers)
