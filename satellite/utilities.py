def calc_year(year):
    twentieth = ('6', '7', '8', '9')
    twenty_first = ('0', '1', '2', '3', '4', '5')
    if year.startswith(twentieth):
        return "19%s" % year
    elif year.startswith(twenty_first):
        return "20%s" % year
    else:
        return year