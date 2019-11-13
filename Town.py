import random
class Town:

    def __init__(self):
        self.firstnum=random.randint(1,10)
        if self.firstnum==1:
            self.first='Blade'
        elif self.firstnum==2:
            self.first='Leaf'
        elif self.firstnum==3:
            self.first='Fire'
        elif self.firstnum==4:
            self.first='Under'
        elif self.firstnum==5:
            self.first='Over'
        elif self.firstnum==6:
            self.first='Frozen'
        elif self.firstnum==7:
            self.first='Dead'
        elif self.firstnum==8:
            self.first='Silver'
        elif self.firstnum==9:
            self.first='Iron'
        elif self.firstnum==10:
            self.first='Dragon'
        self.secondnum=random.randint(1,10)
        if self.secondnum == 1:
            self.second = 'wire'
        elif self.secondnum == 2:
            self.second = 'hill'
        elif self.secondnum == 3:
            self.second = 'gate'
        elif self.secondnum == 4:
            self.second = 'star'
        elif self.secondnum == 5:
            self.second = 'deep'
        elif self.secondnum == 6:
            self.second = 'helm'
        elif self.secondnum == 7:
            self.second = 'run'
        elif self.secondnum == 8:
            self.second = 'mountain'
        elif self.secondnum == 9:
            self.second = 'port'
        elif self.secondnum == 10:
            self.second = 'river'