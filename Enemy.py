import random
class Enemy:

    def __init__(self):
        self.name = random.randint(1, 10)
        if self.name == 1:
            self.name = 'Vale'
        elif self.name == 2:
            self.name = 'John'
        elif self.name == 3:
            self.name = 'Log'
        elif self.name == 4:
            self.name = 'Evenlife'
        elif self.name == 5:
            self.name = 'Jasthorn'
        elif self.name == 6:
            self.name = 'Hailith'
        elif self.name == 7:
            self.name = 'Gongv'
        elif self.name == 8:
            self.name = 'Viklon'
        elif self.name == 9:
            self.name = 'Zadr'
        elif self.name == 10:
            self.name = 'Zailon'

        self.title = random.randint(1, 10)
        if self.title == 1:
            self.title = 'the Great'
        elif self.title == 2:
            self.title = 'the Powerful'
        elif self.title == 3:
            self.title = 'the nobody'
        elif self.title == 4:
            self.title = 'the Overlord'
        elif self.title == 5:
            self.title = 'the Scholar'
        elif self.title == 6:
            self.title = 'the World Eater'
        elif self.title == 7:
            self.title = 'the terrified'
        elif self.title == 8:
            self.title = 'the Elder'
        elif self.title == 9:
            self.title = 'the All Knowing'
        elif self.title == 10:
            self.title = 'the Destined Hero'
