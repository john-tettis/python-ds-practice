def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    lst = list(phrase.split(' '))

    acc =[]
    for word in lst:
        acc.append(word.capitalize())
    return ' '.join(acc)
