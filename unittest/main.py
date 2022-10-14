def add5( num1=0, num2=0):
    try:
        if (num1,num2):
            return int(num1) + int(num2)
    except TypeError:
        return "Enter a no"
    except ValueError as err:
        return err

print(add5(None,None))