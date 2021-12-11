def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    count = 1
    odd_count = []

    for num in nums:
        if num % 2 == 0:
            count = count * num
        elif num % 2 == 1:
            odd_count.append(num)

    if odd_count == nums:
        return 1
    else:
        return count
