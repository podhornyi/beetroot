import unittest

from models import Boss, Worker


class TestWorker(unittest.TestCase):

    # def setUpClass(a):
    #     print('setUpClass')

    def setUp(self):
        self.boss = Boss(1, 'Kola', 'Noname')
        self.worker = Worker(1, 'Ivan', 'Noname', self.boss)

    def test_worker_init_boos(self):
        self.assertEqual(self.worker.boss, self.boss)

    def test_worker_change_boss(self):
        self.assertEqual(self.worker.boss, self.boss)
        changed_boss = Boss(2, 'X', '')
        self.worker.boss = changed_boss

        self.assertNotEqual(self.worker.boss, self.boss)
        self.assertEqual(self.worker.boss, changed_boss)

