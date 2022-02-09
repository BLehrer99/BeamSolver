def get_loads():
    user_input = "new load"
    loads_array = []
    while(user_input != "end"):
        user_input = input("Enter load type or 'end' once all forces are inputted ('moment', 'point', 'distributed', 'ramp') ")
         
        if user_input == "moment":
            location = eval(input("Enter moment location (m) "))
            magnitude = eval(input("Enter the magnitude of the moment (Nm, clockwise is positive) "))
            loads_array.append(Load("moment", location, 0, 0, 0, magnitude))
            continue
        
        if user_input == "point":
            location = eval(input("Enter point force location (m) "))
            magnitude = eval(input("Enter the magnitude of the point force (N, up is positive) "))
            loads_array.append(Load("point", location, 0, magnitude, 0, 0))
            continue

        if user_input == "distributed":
            startLoc = eval(input("Enter distributed force start location (m) "))
            endLoc = eval(input("Enter distributed force end location (m) "))
            magnitude = eval(input("Enter the magnitude of the distributed force (N/m, up is positive) "))
            loads_array.append(Load("distributed", startLoc, endLoc, magnitude, 0, 0))
            continue

        if user_input == "ramp":
            startLoc = eval(input("Enter ramp force start location (m) "))
            endLoc = eval(input("Enter ramp force end location (m) "))
            startMag = eval(input("Enter the start magnitude of the ramp force (N, up is positive) "))
            endMag = eval(input("Enter the end magnitude of the ramp force (N, up is positive) "))
            loads_array.append(Load("distributed", startLoc, endLoc, startMag, endMag, 0))
            continue

        if user_input != "end": print("Unknown load type ")

    return loads_array


def find_centroid_force(load):
    if load.type == "moment":
        load.centroid = load.start_loc
        return load

    if load.type == "point":
        load.centroid = load.start_loc
        load.force = load.start_mag
        return load
    
    if load.type == "distributed":
        load.centroid = (load.end_loc + load.start_loc)/2
        load.force = (load.end_loc - load.start_loc) * load.start_mag
        return load
    
    if load.type == "ramp":
        if load.start_mag < load.end_mag:
            load.centroid = load.start_loc + 2 * (load.end_loc - load.start_loc) / 3
        else:
            load.centroid = load.start_loc + (load.end_loc - load.start_loc) / 3

        load.force = ((load.end_loc - load.start_loc) * load.start_mag) + ((load.end_mag - load.start_mag) * (load.end_loc - load.start_loc) / 2)
        return load
    
    print("error in loads.find_centroid_force(): load type not recognized")
    exit()

class Load:
    centroid = 0
    force = 0
    type = "init"

    def __init__(self, type, start_loc, end_loc, start_mag, end_mag, moment):
        self.type = type
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.start_mag = start_mag
        self.end_mag = end_mag
        self.moment = moment
