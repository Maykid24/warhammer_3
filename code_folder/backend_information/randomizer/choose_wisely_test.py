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
        match random_race:
            case "Beastman":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Beastman)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Bretonnia":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Bretonnia)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Chaos Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Chaos_Dwarfs)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Daemons of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Daemons_of_Chaos)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Dark Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dark_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dwarfs)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "The Empire":
                Race = random_race
                Legendary_Lord = random.choice(r_table.The_Empire)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Grand Cathay":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Grand_Cathay)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Greenskins":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Greenskins)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "High Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.High_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Khorne":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Khorne)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Kislev":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Kislev)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Lizardmen":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Lizardmen)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Norsca":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Norsca)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Nurgle":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Nurgle)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))   
            case "Ogre Kingdoms":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Ogre_Kingdoms)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Skaven":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Skaven)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Slaanesh":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Slaanesh)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Tomb Kings":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tomb_Kings)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Tzeentch":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tzeentch)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Vampire Coast":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Coast)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Vampire Counts":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Counts)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Warriors of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Warriors_of_Chaos)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Wood Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Wood_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
    elif previous_race.lower() == "none":
        random_race = random.choice(r_table.Races)
        match random_race:
            case "Beastman":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Beastman)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Bretonnia":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Bretonnia)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Chaos Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Chaos_Dwarfs)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Daemons of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Daemons_of_Chaos)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Dark Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dark_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Dwarfs":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Dwarfs)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "The Empire":
                Race = random_race
                Legendary_Lord = random.choice(r_table.The_Empire)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Grand Cathay":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Grand_Cathay)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Greenskins":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Greenskins)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "High Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.High_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Khorne":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Khorne)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Kislev":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Kislev)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Lizardmen":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Lizardmen)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Norsca":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Norsca)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Nurgle":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Nurgle)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))   
            case "Ogre Kingdoms":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Ogre_Kingdoms)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Skaven":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Skaven)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Slaanesh":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Slaanesh)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Tomb Kings":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tomb_Kings)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Tzeentch":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Tzeentch)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Vampire Coast":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Coast)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Vampire Counts":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Vampire_Counts)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Warriors of Chaos":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Warriors_of_Chaos)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
            case "Wood Elves":
                Race = random_race
                Legendary_Lord = random.choice(r_table.Wood_Elves)
                print("Race: {}\nLegendary Lord: {}".format(Race, Legendary_Lord))
