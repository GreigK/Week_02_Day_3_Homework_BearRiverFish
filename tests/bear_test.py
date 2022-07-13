import unittest
from src.bear import Bear
from src.fish import Fish
from src.river import River


class TestBear(unittest.TestCase):
    
    def setUp(self):
        self.bear = Bear("Jack", "Black")

    def test_check_bear_name(self):
        self.assertEqual("Jack", self.bear.name)

    def test_check_bear_type(self):
        self.assertEqual('Black', self.bear.type)

    def test_fish_in_stomach(self):
        self.bear.fish_in_stomach()
        self.assertEqual(1, self.bear.stomach)