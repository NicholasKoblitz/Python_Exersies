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
    tl_br = []
    bl_tr = []

    for lst in matrix:

        if len(lst) == 2:
            if matrix[0] == lst:
                tl_br.append(lst[0])
                bl_tr.append(lst[-1])
            elif matrix[-1] == lst:
                tl_br.append(lst[-1])
                bl_tr.append(lst[0])
        else:
            if matrix[0] == lst:
                tl_br.append(lst[0])
                bl_tr.append(lst[-1])
            elif matrix[1] == lst:
                tl_br.append(lst[1])
                bl_tr.append(lst[1])
            elif matrix[-1] == lst:
                tl_br.append(lst[-1])
                bl_tr.append(lst[0])

    tl_br_sum = sum(tl_br)
    bl_tr_sum = sum(bl_tr)
    total = [tl_br_sum, bl_tr_sum]

    total_sum = sum(total)

    return total_sum
