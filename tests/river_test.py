import unittest
from src.fish import Fish
from src.bear import Bear
from src.river import River

class TestRiver(unittest.TestCase):
    
    def setUp(self):
        self.river = River("Amazon")

    def test_check_river_name(self):
        self.assertEqual("Amazon", self.river.name)

    def food_count(self):
        return len(self.food_count)