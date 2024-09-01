import sys
import os
import random

os.chdir("code_folder/")
sys.path.append(os.getcwd())

import backend_information.races.race_table as r_table

def random_pick():
    previous_race = input("What was your last race you played or None? ").strip().lower()

    if previous_race != "none":
        if previous_race.capitalize() in r_table.Races:
            r_table.Races.remove(previous_race.capitalize())

    random_race = random.choice(r_table.Races)
    print("Race:", random_race)
    
    # Assuming that each race has an equivalent list in r_table
    race_dict = {
        "Beastman": r_table.Beastman,
        "Bretonnia": r_table.Bretonnia,
        "Chaos Dwarfs": r_table.Chaos_Dwarfs,
        "Daemons of Chaos": r_table.Daemons_of_Chaos,
        "Dark Elves": r_table.Dark_Elves,
        "Dwarfs": r_table.Dwarfs,
        "The Empire": r_table.The_Empire,
        "Grand Cathay": r_table.Grand_Cathay,
        "Greenskins": r_table.Greenskins,
        "High Elves": r_table.High_Elves,
        "Khorne": r_table.Khorne,
        "Kislev": r_table.Kislev,
        "Lizardmen": r_table.Lizardmen,
        "Norsca": r_table.Norsca,
        "Nurgle": r_table.Nurgle,
        "Ogre Kingdoms": r_table.Ogre_Kingdoms,
        "Skaven": r_table.Skaven,
        "Slaanesh": r_table.Slaanesh,
        "Tomb Kings": r_table.Tomb_Kings,
        "Tzeentch": r_table.Tzeentch,
        "Vampire Coast": r_table.Vampire_Coast,
        "Vampire Counts": r_table.Vampire_Counts,
        "Warriors of Chaos": r_table.Warriors_of_Chaos,
        "Wood Elves": r_table.Wood_Elves
    }
    
    if random_race in race_dict:
        print("Legendary Lord:", random.choice(race_dict[random_race]))
    else:
        print("No such race found.")

random_pick()
