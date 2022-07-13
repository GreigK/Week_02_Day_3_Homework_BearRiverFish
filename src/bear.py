class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = 0

    def check_bear_name(self):
        return self.name

    def check_bear_type(self):
        return self.type

    def food_count(self):
        return len(self.stomach)

    def fish_in_stomach(self):
        self.stomach += 1