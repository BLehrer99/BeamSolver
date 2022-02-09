def solve_reactions(supports_array = [], loads_array = []):
    
    if supports_array[0].type == "fixed":
        #sum forces
        sum_forces = 0
        for load in loads_array:
            sum_forces += load.force

        supports_array[0].force = -1 * sum_forces

        #sum moments about fixed support
        sum_moments = 0
        for load in loads_array:
            sum_moments += load.moment
            sum_moments -= load.force * load.centroid
        supports_array[0].moment = -1 * sum_moments
    
        return supports_array

    if supports_array[0].type == "pinned":
        #sum moments about support a
        offset = -supports_array[0].xLoc
        sum_moments = 0
        for load in loads_array:
            sum_moments += load.moment
            sum_moments -= load.force * (load.centroid + offset)
        supports_array[1].force = sum_moments / (supports_array[1].xLoc + offset)

        #sum forces
        sum_forces = supports_array[1].force
        for load in loads_array:
            sum_forces += load.force
        supports_array[0].force = -1 * sum_forces
    
        return supports_array

    print("error in reactions.solve_reactions(): support type not recognized")
    exit()
