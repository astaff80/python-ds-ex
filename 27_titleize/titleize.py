def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    p = phrase.split(" ")
    t = []

    for w in p:
        t.append(w.lower().capitalize())

    return " ".join(t)
