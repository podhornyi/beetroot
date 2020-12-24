import unittest
import pytest

from models import Boss, Worker


@pytest.fixture
def boss_builer():
    def boss(id, name, company):
        return Boss(id, name, company)
    return boss


def test_someting(boss_builer):
    boss1 = boss_builer(1, 'Kola', 'Inc 1')
    assert boss1.id == 1


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

