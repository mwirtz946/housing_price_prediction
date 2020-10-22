def array_to_dict(labels,coeffs):
    '''
    This function takes two arrays as arguments and turns those 
    arrays into a dictionary so that it is easier to interpret the 
    coefficients from the sklearn analysis
    '''
    one_list = list(labels)
    two_list = list(coeffs)
    res = {} 
    for key in two_list: 
        for name in one_list: 
            res[key] = name 
            one_list.remove(name) 
            break 
    return res