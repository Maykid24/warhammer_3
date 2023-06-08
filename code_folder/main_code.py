# This file is to bring functions up to the front for ease of use
# This way all other files will need to be updated for updates instead of this main file
from datetime import datetime


# import backend_information.randomizer.choose_wisely as c_wisely
import backend_information.randomizer.choose_wisely_test as c_wisely_v2

def write_file(data):
    with open("C:/Users/patjs/Desktop/Warhammer_Race_Pick.txt", "w") as f:
        f.writelines(data)
        f.close()

def run():
    data = c_wisely_v2.random_pick()
    write_file(data)

run()
