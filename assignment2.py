def isHappy(num):
    try:
        num = float(num)
        if num > 0 and num % 1 == 0:
            return True
        else:
            return False
    except:
        return False
    