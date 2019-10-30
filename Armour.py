import random
class Armour:

    def __init__(self):
        self.Suit =random.randint(1, 20)
        if self.Suit == 1:
            self.Suit = 'Light Leather Armour'
        elif self.Suit == 2:
            self.Suit = 'Medium Leather Armour'
        elif self.Suit == 3:
            self.Suit = 'Heavy Leather Armour'
        elif self.Suit == 4:
            self.Suit = 'Light Steel Armour'
        elif self.Suit == 5:
            self.Suit = 'Medium Steel Armour'
        elif self.Suit == 6:
            self.Suit = 'Heavy Steel Armour'
        elif self.Suit == 7:
            self.Suit = 'Light Mithril Armour'
        elif self.Suit == 8:
            self.Suit = 'Medium Mithril Armour'
        elif self.Suit == 9:
            self.Suit = 'Heavy Mithril Armour'
        elif self.Suit == 10:
            self.Suit = 'Light Daedric Armour'
        elif self.Suit == 11:
                self.Suit = 'Medium Daedric Armour'
        elif self.Suit == 12:
                self.Suit = 'Heavy Daedric Armour'
        elif self.Suit == 13:
                self.Suit = 'Light Gold Armour'
        elif self.Suit == 14:
                self.Suit = 'Medium Gold Armour'
        elif self.Suit == 15:
                self.Suit = 'Heavy Gold Armour'
        elif self.Suit == 16:
                self.Suit = 'Light Silver Armour'
        elif self.Suit == 17:
                self.Suit = 'Medium Silver Armour'
        elif self.Suit == 18:
                self.Suit = 'Heavy Silver Armour'
        elif self.Suit == 19:
                self.Suit = 'Fire Lord Armour'
        elif self.Suit == 20:
                self.Suit = 'Ice Lord Armour'
