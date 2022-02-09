def getSupports():
    supportsArray = []
    supportType = input("Enter support type ('simply supported' or 'fixed') ").lower()
    if supportType == "simply supported ":
        supportALoc = eval(input("Enter the location of support A (m) "))
        supportBLoc = eval(input("Enter the location of support B (m) "))
        #create new pair of pinned/roller supports
        supportsArray.append(Support(supportALoc, "pinned"))
        supportsArray.append(Support(supportBLoc, "pinned"))
        return supportsArray

    elif supportType == "cantilever" or supportType == "fixed":
        supportsArray.append(Support(0, "fixed"))
        return supportsArray

    else:
        print("Error - unknown input ")
        getSupports()

class Support:
    force = 0
    moment = 0

    def __init__(self, x, type):
        self.xLoc = x
        self.type = type
    