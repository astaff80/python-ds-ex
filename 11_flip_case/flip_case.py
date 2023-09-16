def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new = []
    for p in phrase: 
        if p == to_swap.lower() or p == to_swap.upper():
            new.append(p.upper()) if p.islower() else new.append(p.lower())
        else:
            new.append(p)
    return "".join(new)
