def distance_from_zero(z):
    if type(z) == int or type(z) == float:
        return abs(z)
    else:
        return "Nope"