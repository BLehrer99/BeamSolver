def getLoads():
    userInput = "new load"
    loadsArray = []
    while(userInput != "end"):
        userInput = input("Enter load type or 'end' once all forces are inputted ('moment', 'point', 'distributed', 'ramp') ")
         
        if userInput == "moment":
            location = eval(input("Enter moment location (m) "))
            magnitude = eval(input("Enter the magnitude of the moment (Nm, clockwise is positive) "))
            loadsArray.append(Load("moment", location, 0, 0, 0, magnitude))
            continue
        
        if userInput == "point":
            location = eval(input("Enter point force location (m) "))
            magnitude = eval(input("Enter the magnitude of the point force (N, up is positive) "))
            loadsArray.append(Load("point", location, 0, magnitude, 0, 0))
            continue

        if userInput == "distributed":
            startLoc = eval(input("Enter distributed force start location (m) "))
            endLoc = eval(input("Enter distributed force end location (m) "))
            magnitude = eval(input("Enter the magnitude of the distributed force (N/m, up is positive) "))
            loadsArray.append(Load("distributed", startLoc, endLoc, magnitude, 0, 0))
            continue

        if userInput == "ramp":
            startLoc = eval(input("Enter ramp force start location (m) "))
            endLoc = eval(input("Enter ramp force end location (m) "))
            startMag = eval(input("Enter the start magnitude of the ramp force (N, up is positive) "))
            endMag = eval(input("Enter the end magnitude of the ramp force (N, up is positive) "))
            loadsArray.append(Load("distributed", startLoc, endLoc, startMag, endMag, 0))
            continue

        print("Unknown load type ")

    return loadsArray


def findCentroid_Force(load):
    if load.type == "moment":
        load.centroid = load.startLoc
        return load

    if load.type == "point":
        load.centroid = load.startLoc
        load.force = load.startMag
        return load
    
    if load.type == "distributed":
        load.centroid = (load.endLoc + load.startLoc)/2
        load.force = (load.endLoc - load.startLoc) * load.startMag
        return load
    
    if load.type == "ramp":
        if load.startMag < load.endMag:
            load.centroid = load.startLoc + 2 * (load.endLoc - load.startLoc) / 3
        else:
            load.centroid = load.startLoc + (load.endLoc - load.startLoc) / 3

        load.force = ((load.endLoc - load.startLoc) * load.startMag) + ((load.endMag - load.startMag) * (load.endLoc - load.startLoc) / 2)
        return load
    
    print("error in loads.findCentroid_Force()")
    exit()

class Load:
    centroid = 0
    force = 0
    type = "init"

    def __init__(self, type, startLoc, endLoc, startMag, endMag, moment):
        self.type = type
        self.startLoc = startLoc
        self.endLoc = endLoc
        self.startMag = startMag
        self.endMag = endMag
        self.moment = moment
