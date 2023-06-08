#This file will be made to randomize all races and choose a legendary lord at random
import sys
import os
import random
from datetime import datetime

os.chdir("code_folder/")
sys.path.append(os.getcwd())


import backend_information.races.race_table as r_table

current_day = datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def random_pick():
    previous_race = input("What was your last race you played or None? ")
    if previous_race.lower() != "none":
        r_table.Races.remove(previous_race)
        random_race = random.choice(r_table.Races)
        match random_race:
            case "Beastman":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Beastman)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Bretonnia":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Bretonnia)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Chaos Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Chaos_Dwarfs)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Daemons of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Daemons_of_Chaos)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Dark Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dark_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dwarfs)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "The Empire":
                Race = random_race
                Legendary_Lord = random.choice(r_table.The_Empire)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Grand Cathay":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Grand_Cathay)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Greenskins":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Greenskins)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "High Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.High_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Khorne":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Khorne)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Kislev":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Kislev)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Lizardmen":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Lizardmen)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Norsca":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Norsca)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Nurgle":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Nurgle)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result   
            case "Ogre Kingdoms":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Ogre_Kingdoms)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Skaven":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Skaven)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Slaanesh":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Slaanesh)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Tomb Kings":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tomb_Kings)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Tzeentch":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tzeentch)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Vampire Coast":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Coast)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Vampire Counts":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Counts)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Warriors of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Warriors_of_Chaos)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Wood Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Wood_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
    elif previous_race.lower() == "none":
        random_race = random.choice(r_table.Races)
        match random_race:
            case "Beastman":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Beastman)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Bretonnia":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Bretonnia)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Chaos Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Chaos_Dwarfs)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Daemons of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Daemons_of_Chaos)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Dark Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dark_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dwarfs)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "The Empire":
                Race = random_race
                Legendary_Lord = random.choice(r_table.The_Empire)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Grand Cathay":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Grand_Cathay)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Greenskins":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Greenskins)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "High Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.High_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Khorne":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Khorne)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Kislev":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Kislev)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Lizardmen":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Lizardmen)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Norsca":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Norsca)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Nurgle":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Nurgle)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result   
            case "Ogre Kingdoms":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Ogre_Kingdoms)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Skaven":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Skaven)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Slaanesh":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Slaanesh)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Tomb Kings":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tomb_Kings)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Tzeentch":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tzeentch)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Vampire Coast":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Coast)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Vampire Counts":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Counts)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Warriors of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Warriors_of_Chaos)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
            case "Wood Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Wood_Elves)
                result = ["Race: {}\nLegendary Lord: {}\n{}".format(Race, Legendary_Lord, current_day)]
                return result
