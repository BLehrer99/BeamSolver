import global_functions

def get_supports():
    supports_array = []
    support_type = input("enter support type ('simply supported' or 'fixed') ").lower()
    if support_type == "simply supported":
        support_a_loc = eval(input("enter the location of support A (m) "))
        support_b_loc = eval(input("enter the location of support B (m) "))
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
        self.x_loc = x
        self.type = type
    
    def load_at_point(self, x):
        return self.moment * global_functions.macaulay(x, self.x_loc, -2) + self.force * global_functions.macaulay(x, self.x_loc, -1)
       
        
    def shear_at_point(self, x):
        return self.moment * global_functions.macaulay(x, self.x_loc, -1) + self.force * global_functions.macaulay(x, self.x_loc, 0)

    def moment_at_point(self, x):
        return self.moment * global_functions.macaulay(x, self.x_loc, 0) + self.force * global_functions.macaulay(x, self.x_loc, 1)

    def macaulay(self, x, a, exp):
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
