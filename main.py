import numpy as np
import math
from os import system

#import other program files
import loads
import reactions
import supports
import global_functions

system('cls')

def get_beam_length():
    user_input = input("enter beam length (m) ")
    if global_functions.is_number(user_input):
        BEAM_LENGTH = eval(user_input)
    else:
        print("error in main.get_beam_length(): input is not numeric")
        return get_beam_length()
    return BEAM_LENGTH

BEAM_LENGTH = get_beam_length()

print("\n")
supports_array = supports.get_supports()

print("\n")
loads_array = loads.get_loads()

for load in loads_array: load.find_centroid_force()

supports_array = reactions.solve_reactions(supports_array, loads_array)

#print reaction forces
print("\nreaction Forces:")
print(f"support A force: {supports_array[0].force} N")
print(f"support A moment: {supports_array[0].moment} Nm")

if len(supports_array) > 1: 
    print(f"support B force: {supports_array[1].force} N")
    print(f"support B moment: {supports_array[1].moment} Nm")
else:
    print("no support B")

#ask user for point to consider conditions at
STEP = 0.0001
shear_force, bending_moment, x_v, x_m, is_mag = global_functions.find_shear_moment(loads_array, supports_array, BEAM_LENGTH, STEP)
if x_v <= STEP: x_v = 0.0
print("\nbending Moments & Shear Forces:")

#fix some annoying rounding things using weird math
round_shear_to = math.ceil(abs(math.log10(STEP))) - math.ceil(math.log10(shear_force)) - 1
shear_force = round(shear_force, round_shear_to)

round_moment_to = math.ceil(abs(math.log10(STEP))) - math.ceil(math.log10(bending_moment)) - 1
bending_moment = round(bending_moment, round_moment_to)

print(f"{is_mag}shear force at point {x_v} m: {shear_force} N")
print(f"{is_mag}bending moment at point {x_m} m: {bending_moment} Nm")

#ask about moments of inertia/cross sections
global_functions.calculate_stesses(shear_force, bending_moment)

print("\n")
exit()
