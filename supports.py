def get_supports():
    supports_array = []
    support_type = input("Enter support type ('simply supported' or 'fixed') ").lower()
    if support_type == "simply supported":
        support_a_loc = eval(input("Enter the location of support A (m) "))
        support_b_loc = eval(input("Enter the location of support B (m) "))
        #create new pair of pinned/roller supports
        supports_array.append(Support(support_a_loc, "pinned"))
        supports_array.append(Support(support_b_loc, "pinned"))
        return supports_array

    if support_type == "cantilever" or support_type == "fixed":
        supports_array.append(Support(0, "fixed"))
        return supports_array

    print("error in supports.get_supports(): unknown input ")
    get_supports()

class Support:
    force = 0
    moment = 0

    def __init__(self, x, type):
        self.xLoc = x
        self.type = type
    