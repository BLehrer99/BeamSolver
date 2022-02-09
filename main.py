import matplotlib.pyplot as plt
import numpy as np

#import other program files
import loads
import reactions
import supports

beamLength = int(input("Enter beam length (m) "))

supportsArray = supports.getSupports()

loadsArray = np.array(loads.getLoads())

loadsArray = np.vectorize(loads.findCentroid_Force)(loadsArray)

supportsArray = reactions.solveReactions(supportsArray, loadsArray)

