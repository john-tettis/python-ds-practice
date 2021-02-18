def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    bool = True

    for val in lst:
        bool = False if not isinstance(val,list) else bool
    return bool
