def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0
    first =0
    last= -1
    half = False
    for arr in matrix:
        total+= arr[first]+arr[last]
        num = (len(matrix)-1)/2
        if isinstance(num,int):
            if arr is matrix[num]:
                half=True
            if half:
                first-=1
                last+=1
            else:
                first+=1
                last-=1
    return total

