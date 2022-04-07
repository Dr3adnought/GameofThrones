#!/usr/bin/env python3

# pip install art (https://pypi.org/project/art/)

# import art

import os
# import time

os.system("clear")

gHouses = {
    'House Stark':
    {'house': 'Stark',
     'kingdom': 'The North',
     'castle': 'Winterfell',
     'sigil': 'A running Direwolf on a white field',
     'house motto': 'Winter is Coming',
     'colors': 'grey & white'},

    'House Lannister':
    {'house': 'Lannister',
     'kingdom': 'The Westerlands',
     'castle': 'Casterly Rock',
     'sigil': 'A roaring golden Lion on a Crimson field',
     'house motto': 'Hear Me Roar',
     'colors': 'gold & crimson'},

    'House Arryn':
    {'house': 'Arryn',
     'kingdom': 'The Vale',
     'castle': 'Eyrie',
     'sigil': 'A blue Falcon silhouetting a white moon against a blue sky',
     'house motto': 'As High As Honour',
     'colors': 'blue & white'},

    'House Tyrell':
    {'house': 'Tyrell',
     'kingdom': 'The Reach',
     'castle': 'Highgarden',
     'sigil': 'A large single golden Rose against a green field',
     'house motto': 'Growing Strong',
     'colors': 'old & green'},

    'House Greyjoy':
    {'house': 'Greyjoy',
     'kingdom': 'The Iron Islands',
     'castle': 'Pyke',
     'sigil': 'A gold Kraken against a black abyss',
     'house motto': 'We Do Not Sow',
     'colors': 'gold & black'},

    'House Martell':
    {'house': 'Martell',
     'kingdom': 'Dorne',
     'castle': 'Sunspear',
     'sigil': 'A red sun pierced by a golden spear against an orange background',
     'house motto': 'Unbowed. Unbent. Unbroken',
     'colors': 'red & orange'},

    'House Baratheon':
    {'house': 'Baratheon',
     'kingdom': 'Stormlands',
     'castle': 'Storm\'s End',
     'sigil': 'A crowned black stag on a golden field',
     'house motto': 'Our Is The Fury',
     'colors': 'black & gold'},

    'House Tully':
    {'house': 'Tully',
     'kingdom': 'The Riverlands',
     'castle': 'River Run',
     'sigil': 'A leaping silver trout against a rippling blue and red tide',
     'house motto': 'Family. Duty. Honour.',
     'colors': 'silver, maroon, & blue'},

    'House Targaryen':
    {'house': 'Targaryen',
     'kingdom': 'The Crownlands',
     'castle': 'King\'s Landing',
     'sigil': 'A red three-headed dragon against a black sky',
     'house motto': 'Family. Duty. Honour.',
     'colors': 'red & black'},
}
round = 0
gHouse = 0

print("Welcome to the Seven Kingdoms.  To which Great House do you belong?\n")

# time.sleep(4)
print("Bloodfly take your tongue?  -- speak, imbecile!\n")

# time.sleep(1)
gHouse = input(f"If you wish to ever draw another breath, you'll answer my question - To which Great House do you belong?  ").strip().capitalize()

while round < 2 and gHouse != ["Targeryen", "Lannister", "Stark", "Tully", "Baratheon", "Martell", "Tyrell", "Greyjoy", "Arryn"]:

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
            f"Ah, House {gHouse}, a traveller from {gHouses.values['kingdom']} visits.")

else:
    print("You may pass!")
    print(
        f"Ah, House {gHouse}, a traveller from {gHouses.values['kingdom']} visits.")
