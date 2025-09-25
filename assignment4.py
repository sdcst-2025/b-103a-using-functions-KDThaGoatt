import math

def isPythagoreanTriple(a,b,c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        return False
    
    values = [a,b,c]
    values = sorted(values)

    if math.sqrt(values[0]**2 + values[1]**2) == values[2]:
        return True
    else:
        return False
    