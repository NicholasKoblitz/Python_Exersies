def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    nums1 = {}
    nums2 = {}
    val1 = []
    val2 = []

    for digit in str(num1):
        if digit not in nums1.keys():
            nums1.update({digit: 1})
        else:
            nums1[digit] += 1

    for digit in str(num2):
        if digit not in nums2.keys():
            nums2.update({digit: 1})
        else:
            nums2[digit] += 1

    new_nums1 = nums1.items()
    new_nums2 = nums2.items()

    if new_nums1 == new_nums2:
        return True
    else:
        return False
