def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = list(phrase)

    new_list = []

    for char in phrase:
        if char == to_swap or char == to_swap.swapcase():
            new_list.append(char.swapcase())
        else:
            new_list.append(char)

    return ''.join(new_list)
