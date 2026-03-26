import random
def rolld20():
    return int(random.randint(1,20))
def rolld6():
    return int(random.randint(1,6))

def mult_rolld6(numdice):
    total=0
    for i in range(numdice):
        total +=random.randint(1, 6)
    return int(total)