class River:
    def __init__(self, name):
        self.name = name
        self.food_count = 0


    def check_river_name(self):
        return self.name

    def food_count(self):
        return len(self.food_count)