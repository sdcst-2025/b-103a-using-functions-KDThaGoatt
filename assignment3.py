import math

def isPerfectSquare(num):

    try:
        num = float(num)
    except:
        return False
    
    if num < 0:
        return False

    sqrtNum = math.sqrt(num)

    if sqrtNum % 1 == 0:
        return True
    else: 
        return False
    