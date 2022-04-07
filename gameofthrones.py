#!/usr/bin/env python3

# pip install art (https://pypi.org/project/art/)

# import art

import os
import time

os.system("clear")

gHouses = {
    'Stark':
    {'house': 'Stark',
     'kingdom': 'The North',
     'castle': 'Winterfell',
     'sigil': 'A running Direwolf on a white field',
     'motto': 'Winter is Coming',
     'colors': 'grey & white'},

    'Lannister':
    {'house': 'Lannister',
     'kingdom': 'The Westerlands',
     'castle': 'Casterly Rock',
     'sigil': 'A roaring golden Lion on a Crimson field',
     'motto': 'Hear Me Roar',
     'colors': 'gold & crimson'},

    'Arryn':
    {'house': 'Arryn',
     'kingdom': 'The Vale',
     'castle': 'Eyrie',
     'sigil': 'A blue Falcon silhouetting a white moon against a blue sky',
     'motto': 'As High As Honour',
     'colors': 'blue & white'},

    'Tyrell':
    {'house': 'Tyrell',
     'kingdom': 'The Reach',
     'castle': 'Highgarden',
     'sigil': 'A large single golden Rose against a green field',
     'motto': 'Growing Strong',
     'colors': 'old & green'},

    'Greyjoy':
    {'house': 'Greyjoy',
     'kingdom': 'The Iron Islands',
     'castle': 'Pyke',
     'sigil': 'A gold Kraken against a black abyss',
     'motto': 'We Do Not Sow',
     'colors': 'gold & black'},

    'Martell':
    {'house': 'Martell',
     'kingdom': 'Dorne',
     'castle': 'Sunspear',
     'sigil': 'A red sun pierced by a golden spear against an orange background',
     'motto': 'Unbowed. Unbent. Unbroken',
     'colors': 'red & orange'},

    'Baratheon':
    {'house': 'Baratheon',
     'kingdom': 'Stormlands',
     'castle': 'Storm\'s End',
     'sigil': 'A crowned black stag on a golden field',
     'motto': 'Our Is The Fury',
     'colors': 'black & gold'},

    'Tully':
    {'house': 'Tully',
     'kingdom': 'The Riverlands',
     'castle': 'River Run',
     'sigil': 'A leaping silver trout against a rippling blue and red tide',
     'motto': 'Family. Duty. Honour.',
     'colors': 'silver, maroon, & blue'},

    'Targaryen':
    {'house': 'Targaryen',
     'kingdom': 'The Crownlands',
     'castle': 'King\'s Landing',
     'sigil': 'A red three-headed dragon against a black sky',
     'motto': 'Family. Duty. Honour.',
     'colors': 'red & black'},
}
round = 0
gHouse = 0

print("Welcome to the Seven Kingdoms.  To which Great House do you belong?\n")
# print(gHouses[gHouse]["house"])

# time.sleep(3)
print("Bloodfly take your tongue?  -- speak, imbecile!\n")

# time.sleep(1.5)
gHouse = input(f"If you wish to ever draw another breath, you'll answer my question - To which Great House do you belong?  ").strip().capitalize()

while round < 2 and gHouse != ["Targaryen", "Lannister", "Stark", "Tully", "Baratheon", "Martell", "Tyrell", "Greyjoy", "Arryn"]:

    if gHouse not in gHouses:
        vassal = input(
            f"\nI've not heard of that house. Is it a vassal to one of the Great Houses in the Seven Kingdoms? ").strip().lower()

        if vassal.lower() != "yes":
            print("\nUnless words to explain your presence here begin to flow from the hole in your face, or you leave now, you had best draw your weapon and prepare for battle.")

        elif vassal.lower() == "yes":
            gHouse = input(
                "\nNow tell me, to which Great House does your vassal pledge itself? ").strip().capitalize()
            round = 2

    else:
        print(
            f"Ah, House {gHouse}, a traveller from {gHouses(gHouse).kingdom} visits.")
        break

else:
    print("You may pass!")
    # print(f"Ah, House {gHouse}, a traveller from {gHouses.values['kingdom']} visits.")
