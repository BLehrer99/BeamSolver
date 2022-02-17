import numpy as np

def find_shear_moment(loads_array, supports_array, BEAM_LENGTH, STEP):
    user_input = input("\nenter point to consider conditions at (m), 'max', 'min', or 'mag' to determine their respective locations ")

    x_v = 0.0
    x_m = 0.0
    v_x = 0.0
    m_x = 0.0

    is_mag = ""

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
            if abs(shear) > v_x:
                v_x = abs(shear)
                x_v = i    
            if abs(moment) > m_x:
                m_x = abs(moment)
                x_m = i
            is_mag = "magnitude of "

    elif is_number(user_input):
        x_v = eval(user_input)
        x_m = x_v
        v_x, m_x = solve_singularity(x_v)
        
    else:
        print("error in golbal_functions.find_shear_moment(): unknown input")
        return find_shear_moment(loads_array, supports_array, BEAM_LENGTH)
    
    return v_x, m_x, x_v, x_m, is_mag


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
    return