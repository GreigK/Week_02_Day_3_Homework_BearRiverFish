import unittest
from src.fish import Fish
from src.bear import Bear
from src.river import River


class TestFish(unittest.TestCase):
    
    def setUp(self):
        self.fish = Fish("James")

    def test_check_fish_name(self):
        self.assertEqual("James", self.fish.name)



