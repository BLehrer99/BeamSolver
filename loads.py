import global_functions

def get_loads():
    user_input = "new load"
    loads_array = []
    torques_array = []

    while(user_input != "end"):
        user_input = input("enter load type or 'end' once all forces are inputted ('moment', 'point', 'distributed', 'torque' (fixed only)) ")
         
        if user_input == "moment":
            location = eval(input("enter moment location (m) "))
            magnitude = eval(input("enter the magnitude of the moment (Nm, clockwise is positive) "))
            loads_array.append(Load("moment", location, 0, 0, 0, magnitude))
            continue
        
        if user_input == "point":
            location = eval(input("enter point force location (m) "))
            magnitude = eval(input("enter the magnitude of the point force (N, up is positive) "))
            loads_array.append(Load("point", location, 0, magnitude, 0, 0))
            continue

        if user_input == "distributed":
            startLoc = eval(input("enter distributed force start location (m) "))
            endLoc = eval(input("enter distributed force end location (m) "))
            magnitude = eval(input("enter the magnitude of the distributed force (N/m, up is positive) "))
            loads_array.append(Load("distributed", startLoc, endLoc, magnitude, 0, 0))
            continue

        if user_input == "torque":
            location = eval(input("enter torque location (m) "))
            magnitude = eval(input("enter the magnitude of the torque (N/m, right hand rule about x-axis) "))
            torques_array.append(Torque(location, magnitude))
            continue

        if user_input == "ramp":
            startLoc = eval(input("enter ramp force start location (m) "))
            endLoc = eval(input("enter ramp force end location (m) "))
            startMag = eval(input("enter the start magnitude of the ramp force (N, up is positive) "))
            endMag = eval(input("enter the end magnitude of the ramp force (N, up is positive) "))

            #break ramp load into a distributed overlayed with a ramp
            loads_array.append(Load("distributed", startLoc, endLoc, startMag, 0, 0))
            loads_array.append(Load("ramp", startLoc, endLoc, 0, endMag-startMag, 0))
            continue

        if user_input != "end": print("unknown load type ")

    return loads_array, torques_array

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

    def find_centroid_force(self):
        if self.type == "moment":
            self.centroid = self.start_loc
            return

        if self.type == "point":
            self.centroid = self.start_loc
            self.force = self.start_mag
            return
        
        if self.type == "distributed":
            self.centroid = (self.end_loc + self.start_loc)/2
            self.force = (self.end_loc - self.start_loc) * self.start_mag
            return
        
        if self.type == "ramp":
            self.centroid = self.start_loc + 2 * (self.end_loc - self.start_loc) / 3

            self.force = ((self.end_loc - self.start_loc) * self.start_mag) + ((self.end_mag - self.start_mag) * (self.end_loc - self.start_loc) / 2)
            return

        return

    def load_at_point(self, x):
        if self.type == "moment":
            return self.moment * global_functions.macaulay(x, self.start_loc, -2)
        if self.type == "point":
            return self.start_mag * global_functions.macaulay(x, self.start_loc, -1)
        if self.type == "distributed":
            return self.start_mag * global_functions.macaulay(x, self.start_loc, 0) - self.start_mag * global_functions.macaulay(x, self.end_loc, 0)
        
    def shear_at_point(self, x):
        if self.type == "moment":
            return self.moment * global_functions.macaulay(x, self.start_loc, -1)
        if self.type == "point":
            return self.start_mag * global_functions.macaulay(x, self.start_loc, 0)
        if self.type == "distributed":
            return self.start_mag * global_functions.macaulay(x, self.start_loc, 1) - self.start_mag * global_functions.macaulay(x, self.end_loc, 1)

    def moment_at_point(self, x):
        if self.type == "moment":
            return self.moment * global_functions.macaulay(x, self.start_loc, 0)
        if self.type == "point":
            return self.start_mag * global_functions.macaulay(x, self.start_loc, 1)
        if self.type == "distributed":
            return self.start_mag * 0.5 * global_functions.macaulay(x, self.start_loc, 2) - self.start_mag * 0.5 * global_functions.macaulay(x, self.end_loc, 2)

class Torque:
    location = 0
    magnitude = 0

    def __init__(self, location, magnitude):
        self.location = location
        self.magnitude = magnitude

