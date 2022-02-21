import numpy as np

def find_shear_moment(loads_array, supports_array, BEAM_LENGTH, STEP):
    user_input = input("\nenter point to consider conditions at (m), 'max', 'min', or 'mag' to determine their respective locations ")

    x_v = 0.0
    x_m = 0.0
    v_x = 0.0
    m_x = 0.0

    def solve_singularity(loc):
        v_x = 0.0
        m_x = 0.0
        for load in loads_array: v_x += load.shear_at_point(loc)
        for support in supports_array: v_x += support.shear_at_point(loc)
        for load in loads_array: m_x += load.moment_at_point(loc)
        for support in supports_array: m_x += support.moment_at_point(loc)
        return v_x, m_x

    if user_input == "max":
        for i in np.arange(0.0, BEAM_LENGTH, STEP):
            shear, moment = solve_singularity(i)
            if shear > v_x:
                v_x = shear
                x_v = i    
            if moment > m_x:
                m_x = moment
                x_m = i

    elif user_input == "min":
        for i in np.arange(0.0, BEAM_LENGTH, STEP):
            shear, moment = solve_singularity(i)
            if shear < v_x:
                v_x = shear
                x_v = i    
            if moment < m_x:
                m_x = moment
                x_m = i

    elif user_input == "mag":
        for i in np.arange(0.0, BEAM_LENGTH, STEP):
            shear, moment = solve_singularity(i)
            if abs(shear) > abs(v_x):
                v_x = shear
                x_v = i    
            if abs(moment) > abs(m_x):
                m_x = moment
                x_m = i

    elif is_number(user_input):
        x_v = eval(user_input)
        x_m = x_v
        v_x, m_x = solve_singularity(x_v)
        
    else:
        print("error in global_functions.find_shear_moment(): unknown input")
        return find_shear_moment(loads_array, supports_array, BEAM_LENGTH)
    
    return v_x, m_x, x_v, x_m


def macaulay(x, a, exp):
    match(exp):
        case -2:
            if x != a: return 0
            return 1 # math.inf
        case -1:
            if x != a: return 0
            return 1 # math.inf
        case 0:
            if x < a: return 0
            return 1
        case 1:
            if x < a: return 0
            return x - a
        case 2:
            if x < a: return 0
            return pow(x - a, 2)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate_stresses(shear_force, bending_moment):
    I = 0
    c = 0

    shear_stress = 0

    shape_input = input("enter the cross section 'rectangular' or 'circular' ")
    if shape_input == "rectangular":
        base_input = input("enter the base of the rectangle (m) ")
        if is_number(base_input):
            base = eval(base_input)
        else:
            print("error in global_functions.calculate_stress(): base is NaN")
            calculate_stresses(shear_force, bending_moment)
            
        height_input = input("enter the height of the rectangle (m) ")
        if is_number(height_input):
            height = eval(height_input)
        else:
            print("error in global_functions.calculate_stress(): height is NaN")
            calculate_stresses(shear_force, bending_moment)

        I = (1/12) * base * pow(height, 3)
        c = height / 2

        shear_stress = 3 * shear_force / (2 * base * height)


    elif shape_input == "circular":
        OD_input = input("enter the OD of the tube (m) ")
        if is_number(OD_input):
            outer = eval(OD_input)
        else:
            print("error in global_functions.calculate_stress(): OD is NaN")
            calculate_stresses(shear_force, bending_moment)
            
        ID_input = input("enter the ID of the tube (m) ")
        if is_number(ID_input):
            inner = eval(ID_input)
        else:
            print("error in global_functions.calculate_stress(): ID is NaN")
            calculate_stresses(shear_force, bending_moment)

        I = (np.pi / 64) * (pow(outer, 4) - pow(inner, 4))
        c = outer / 2
        if inner == 0:
            shear_stress = 4 * shear_force / (3 * np.pi * pow(outer/2, 2))
        else:
            shear_stress = 2 * shear_force / (np.pi * (pow(outer/2, 2) - pow(inner/2, 2)))

    else:
        print("error in global_functions.calculate_stress(): cross section not recognized")
        calculate_stresses(shear_force, bending_moment)

    normal_stress = -bending_moment * c / I

    return shear_stress, normal_stress
