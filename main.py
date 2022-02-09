#import matplotlib

#import other program files
import loads
import reactions
import supports

beamLength = int(input("Enter beam length (m) "))

supportsArray = []
supportsArray = supports.getSupports()

loadsArray = []
loadsArray = loads.getLoads()

loadsArray = loads.findCentroid_Force(loadsArray)

supportsArray = reactions.solveReactions(supportsArray, loadsArray)

