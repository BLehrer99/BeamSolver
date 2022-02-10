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

            loads_array.append(Load("distributed", startLoc, endLoc, startMag, 0, 0))
            loads_array.append(Load("ramp", startLoc, endLoc, 0, endMag-startMag, 0))
            continue

        if user_input != "end": print("Unknown load type ")

    return loads_array

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
            if self.start_mag > self.end_mag:
                self.centroid = self.start_loc + 2 * (self.end_loc - self.start_loc) / 3
            else:
                self.centroid = self.start_loc + (self.end_loc - self.start_loc) / 3

            self.force = ((self.end_loc - self.start_loc) * self.start_mag) + ((self.end_mag - self.start_mag) * (self.end_loc - self.start_loc) / 2)
            return

        return
