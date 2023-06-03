#This file will be made to randomize all races and choose a legendary lord at random
import sys
import os
import random

os.chdir("code_folder/")
sys.path.append(os.getcwd())


import backend_information.races.race_table as r_table


def random_pick():
    previous_race = input("What was your last race you played or None? ")
    if previous_race.lower() != "none":
        r_table.Races.remove(previous_race)
        random_race = random.choice(r_table.Races)
        if random_race == "Beastman":
            print("Race:", random_race)
            print("Legendary Lord:", random.choice(r_table.Beastman))
        elif random_race == "Bretonnia":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Bretonnia))
        elif random_race == "Chaos Dwarfs":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Chaos_Dwarfs))
        elif random_race == "Daemons of Chaos":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Daemons_of_Chaos))
        elif random_race == "Dark Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Dark_Elves))
        elif random_race == "Dwarfs":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Dwarfs))
        elif random_race == "The Empire":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.The_Empire))
        elif random_race == "Grand Cathay":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Grand_Cathay))
        elif random_race == "Greenskins":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Greenskins))
        elif random_race == "High Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.High_Elves))
        elif random_race == "Khorne":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Khorne))
        elif random_race == "Kislev":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Kislev))
        elif random_race == "Lizardmen":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Lizardmen))
        elif random_race == "Norsca":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Norsca))
        elif random_race == "Nurgle":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Nurgle))
        elif random_race == "Ogre Kingdoms":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Ogre_Kingdoms))
        elif random_race == "Skaven":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Skaven))
        elif random_race == "Slaanesh":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Slaanesh))
        elif random_race == "Tomb Kings":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Tomb_Kings))
        elif random_race == "Tzeentch":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Tzeentch))
        elif random_race == "Vampire Coast":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Vampire_Coast))
        elif random_race == "Vampire Counts":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Vampire_Counts))
        elif random_race == "Warriors of Chaos":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Warriors_of_Chaos))
        elif random_race == "Wood Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Wood_Elves))
    elif previous_race.lower() == "none":
        random_race = random.choice(r_table.Races)
        if random_race == "Beastman":
            print("Race:", random_race)
            print("Legendary Lord:", random.choice(r_table.Beastman))
        elif random_race == "Bretonnia":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Bretonnia))
        elif random_race == "Chaos Dwarfs":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Chaos_Dwarfs))
        elif random_race == "Daemons of Chaos":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Daemons_of_Chaos))
        elif random_race == "Dark Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Dark_Elves))
        elif random_race == "Dwarfs":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Dwarfs))
        elif random_race == "The Empire":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.The_Empire))
        elif random_race == "Grand Cathay":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Grand_Cathay))
        elif random_race == "Greenskins":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Greenskins))
        elif random_race == "High Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.High_Elves))
        elif random_race == "Khorne":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Khorne))
        elif random_race == "Kislev":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Kislev))
        elif random_race == "Lizardmen":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Lizardmen))
        elif random_race == "Norsca":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Norsca))
        elif random_race == "Nurgle":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Nurgle))
        elif random_race == "Ogre Kingdoms":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Ogre_Kingdoms))
        elif random_race == "Skaven":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Skaven))
        elif random_race == "Slaanesh":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Slaanesh))
        elif random_race == "Tomb Kings":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Tomb_Kings))
        elif random_race == "Tzeentch":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Tzeentch))
        elif random_race == "Vampire Coast":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Vampire_Coast))
        elif random_race == "Vampire Counts":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Vampire_Counts))
        elif random_race == "Warriors of Chaos":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Warriors_of_Chaos))
        elif random_race == "Wood Elves":
            print("Race:",random_race)
            print("Legendary Lord:", random.choice(r_table.Wood_Elves))
