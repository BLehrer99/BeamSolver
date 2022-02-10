import numpy as np
from os import system

#import other program files
import loads
import reactions
import supports

system('cls')

BEAM_LENGTH = int(input("Enter beam length (m) "))

supports_array = supports.get_supports()

loads_array = loads.get_loads()

for load in loads_array: load.find_centroid_force()

supports_array = reactions.solve_reactions(supports_array, loads_array)

#print reaction forces
print("\nReaction Forces:")
print(f"support A force: {supports_array[0].force}")
print(f"support A moment: {supports_array[0].moment}")

if len(supports_array) > 1: 
    print(f"support B force: {supports_array[1].force}")
    print(f"support B moment: {supports_array[1].moment}")
else:
    print("no support B")

exit()
