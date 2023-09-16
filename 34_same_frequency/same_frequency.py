def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    d1 = {}
    d2 = {}

    for n in str(num1):
        if n in d1:
            d1[n] += 1
        else:
            d1[n] = 1

    for n in str(num2):
        if n in d2:
            d2[n] += 1
        else:
            d2[n] = 1

    return d1 == d2
