def same_frequency(num1, num2):
    if len(str(num1)) == len(str(num2)):
        return True
    else:
        return False
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """