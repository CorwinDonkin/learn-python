import time
import random
from Enemy import Enemy
from Weapon import Weapon
from Armour import Armour
from Town import Town

race=input('What is your race merchant: ')
age=int(input("How old are you?: "))
name=input("Merchant, what is your name? ");
donkey=input("What is your donkey's name? ");

gold=50;
armourstock=0;
weaponstock=0;
house=0;
y=1
print("you have 50 gold")
print("")
while y==1:
    town=Town()
    print("You arrive to the town of",town.first+town.second)
    print("")
    sellbuy=input("Do you want to buy or sell?")
    print("")
    if sellbuy=='buy' or sellbuy=='Buy':
        stock=input("What stock do you want to buy. Weapons: 20 Gold, Armour: 25 Gold. House:100")
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
        elif stock=='house' and gold>=100:
            print("You bought a nice small house.")
            house=house+1
            gold=gold-100
        elif stock=='house':
            print("You don't have enough money to buy a house.")
    elif sellbuy=='sell' or sellbuy=='Sell':
        sell=input("What stock do you want to sell. Weapons, Armour or a house.")
        if sell=='weapons' and weaponstock>=1:
            x=random.randint(19,28)
            gold=gold+x
            weaponstock=weaponstock-1
            print("You sell the stock for",x,"gold")
        elif sell=='weapons':
            print("You don't have any stock to sell")
        elif sell=='armour' and armourstock>=1:
            x=random.randint(24,36)
            gold=gold+x
            armourstock=armourstock-1
            print("You sold the stock for",x,"gold")
        elif sell=='armour':
            print("You don't have any stock to sell")
        elif sell=='house' and house>=1:
            print("You sell a house.",x,"gold.")
            x=random.randint(85,135)
            gold=gold+x
            print("You sell the house for")
            house=house-1
        elif sell=='house':
            print("You don't have a house to sell")

    print("You now have",gold,"gold")
    print("")
