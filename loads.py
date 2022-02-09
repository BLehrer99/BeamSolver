def getLoads():
    userInput = "new load"
    loadsArray = []
    while(1):
        userInput = input("Enter load type or 'end' once all forces are inputted ('moment', 'point', 'distributed', 'ramp') ")
        
        if userInput == "end":
            return loadsArray

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

def findCentroid_Force(loadsArray = []):
    for i in loadsArray:
        if loadsArray[i].type == "moment":
            loadsArray[i].centroid = loadsArray[i].startLoc
            continue

        if loadsArray[i].type == "point":
            loadsArray[i].centroid = loadsArray[i].startLoc
            loadsArray[i].force = loadsArray[i].startMag
            continue
        
        if loadsArray[i].type == "distributed":
            loadsArray[i].centroid = (loadsArray[i].endLoc + loadsArray[i].startLoc)/2
            loadsArray[i].force = (loadsArray[i].endLoc - loadsArray[i].startLoc) * loadsArray[i].startMag
            continue
        
        if loadsArray[i].type == "ramp":
            if loadsArray[i].startMag < loadsArray[i].endMag:
                loadsArray[i].centroid = loadsArray[i].startLoc + 2*(loadsArray[i].endLoc - loadsArray[i].startLoc)/3
            else:
                loadsArray[i].centroid = loadsArray[i].startLoc + (loadsArray[i].endLoc - loadsArray[i].startLoc)/3

            loadsArray[i].force = ((loadsArray[i].endLoc - loadsArray[i].startLoc) * loadsArray[i].startMag) + ((loadsArray[i].endMag - loadsArray[i].startMag) * (loadsArray[i].endLoc - loadsArray[i].startLoc) / 2)
            continue

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
