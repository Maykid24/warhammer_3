# This file is to bring functions up to the front for ease of use
# This way all other files will need to be updated for updates instead of this main file

import backend_information.randomizer.choose_wisely as c_wisely

choice = c_wisely.random_pick()

file1 = open("C:/Users/patjs/Desktop/Warhammer_Race_Pick.txt", "w")
file1.writelines(choice)
file1.close()