import random
class Towngenerator:

    def __init__(self):
        self.first = random.randint(1, 10)
        self.second = random.randint(1, 10)
        if self.first == 1:
            self.first = 'Dragon'
        elif self.first == 2:
            self.first = 'Blade'
        elif self.first == 3:
            self.first = 'Leaf'
        elif self.first == 4:
            self.first = 'Iron'
        elif self.first == 5:
            self.first = 'Silver'
        elif self.first == 6:
            self.first = 'Under'
        elif self.first == 7:
            self.first = 'Over'
        elif self.first == 8:
            self.first = 'Fire'
        elif self.first == 9:
            self.first = 'Ocean'
        else:
            self.first = 'Ice'

        if self.second == 1:
            self.second = 'wire'
        elif self.second == 2:
            self.second == 'dock'
        elif self.second == 3:
            self.second = 'deep'
        elif self.second == 4:
            self.second = 'wind'
        elif self.second == 5:
            self.second = 'end'
        elif self.second == 6:
            self.second = 'gate'
        elif self.second == 7:
            self.second = 'hill'
        elif self.second == 8:
            self.second = 'star'
        elif self.second == 9:
            self.second = 'mountain'
        elif self.second == 10:
            self.second = 'dark'

        self.town=self.first+self.second