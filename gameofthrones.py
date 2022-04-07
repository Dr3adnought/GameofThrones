#!/usr/bin/env python3

# pip install art (https://pypi.org/project/art/)

# import art

from gothouses import gHouses
import os
import time


os.system("clear")


round = 0
gHouse = 0

print("Welcome to the Seven Kingdoms.  To which Great House do you belong?\n")
# print(gHouses[gHouse]["house"])

time.sleep(3)
print("Bloodfly take your tongue?  -- speak, imbecile!\n")

time.sleep(1.5)
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
            f"\nAh, apologies mi-lord, mi-lady -- House {gHouse}, a traveller from {gHouses[gHouse]['kingdom']} visits. My liege!")
        break

else:
    print(
        f"\nAh, yes, House {gHouse}, a traveller from {gHouses[gHouse]['kingdom']} visits.")
    print("\nYou may pass!")
