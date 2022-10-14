def add5( num1, num2):
    try:
        if (num1,num2):
            return int(num1) + int(num2)
    except (AssertionError, ValueError) as err:
        return err
    except TypeError:
        return "Enter a no"
    except ValueError as err:
        return err

