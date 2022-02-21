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
print("\nreaction forces:")
print(f"support A force: {supports_array[0].force} N")
print(f"support A moment: {supports_array[0].moment} Nm")

if len(supports_array) > 1: 
    print(f"support B force: {supports_array[1].force} N")
    print(f"support B moment: {supports_array[1].moment} Nm")
else:
    print("no support B")

#ask user for point to consider conditions at
STEP = 0.00001
shear_force, bending_moment, x_v, x_m = global_functions.find_shear_moment(loads_array, supports_array, BEAM_LENGTH, STEP)
if x_v <= STEP: x_v = 0.0
print("\nbending moments & shear forces:")

#fix some annoying rounding things using weird math
round_shear_to = math.ceil(abs(math.log10(STEP))) - math.ceil(math.log10(abs(shear_force))) - 1
shear_force = round(shear_force, round_shear_to)

round_moment_to = math.ceil(abs(math.log10(STEP))) - math.ceil(math.log10(abs(bending_moment))) - 1
bending_moment = round(bending_moment, round_moment_to)

print(f"shear force at point {x_v} m: {shear_force} N")
print(f"bending moment at point {x_m} m: {bending_moment} Nm")
print("\n")

#ask about moments of inertia/cross sections
shear_stress, normal_stress = global_functions.calculate_stresses(shear_force, bending_moment)
print(f"shear stress on inner edge at point {x_v} m: {shear_stress} Pa")
print(f"normal stress at top of beam at point {x_m} m: {normal_stress} Pa")

print("\n")
exit()
