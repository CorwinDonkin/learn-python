import time
import random
from Towngenerator import Towngenerator
from Enemy import Enemy
town=Towngenerator()
from Weapon import Weapon
from Armour import Armour

race=input('What is your race merchant: ')
age=int(input("How old are you?: "))
name=input("Merchant, what is your name? ");
donkey=input("What is your donkey's name? ");

gold=50;
armourstock=0;
weaponstock=0;
y=1
print("you have 50 gold")
print("")
while y==1:
    sellbuy=input("Do you want to buy or sell items.")
    print("")
    if sellbuy=='buy' or sellbuy=='Buy':
        stock=input("What stock do you want to buy. Weapons: 20 Gold, Armour: 25 Gold ")
        if stock=='weapons' and gold>=20:
            weapon = Weapon()
            print('You bought a',weapon.weapon)
            gold=gold-20
            weaponstock=weaponstock+1
        elif stock=='weapons':
            print("You don't have the funds to purchase this stock")
        elif stock=='armour' and gold>=25:
            armour = Armour()
            print("You bought a set of",armour.Suit)
            gold=gold-25
            armourstock=armourstock+1
        elif stock=='armour':
            print("You don't have the funds to purchase this stock")

    elif sellbuy=='sell' or sellbuy=='Sell':
        sell=input("What stock do you want to sell. Weapons, Armour")
        if sell=='weapons' and weaponstock>=1:
            x=random.randint(19,28)
            gold=gold+x
            weaponstock=weaponstock-1
            print("You sell the stock for",x,"gold")
        elif sell=='weapons':
            print("You don't have any stock to sell")
        elif sell=='armour' and armourstock>=1:
            x=random.randint(24,33)
            gold=gold+x
            armourstock=armourstock-1
            print("You sold the stock for",x,"gold")
        elif sell=='armour':
            print("You don't have any stock to sell")
    print("You now have",gold,"gold")
    print("")
