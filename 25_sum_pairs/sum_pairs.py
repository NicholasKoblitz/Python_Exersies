def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    loops = 0
    added_lst = []
    final_num1 = 0
    final_num2 = 0
    total = 3
    num1_lst = []
    num2_lst = []
    num1 = 0
    num2 = 0
    diff = 0

    while loops < len(nums):
        held_num = nums[loops]
        for num in nums:
            if held_num + num == goal:
                if loops == 0:
                    added_lst.append((held_num, num))
                else:
                    if (num, held_num) not in added_lst:
                        added_lst.append((held_num, num))

        loops += 1

    # tup_lst = tuple(added_lst)
    # for item in added_lst:

    for num1, num2 in added_lst:
        num_idx1 = nums.index(num1)
        num1_lst.append(num_idx1)
        num_idx2 = nums.index(num2)
        num2_lst.append(num_idx2)
        diff = num_idx2 - num_idx1

        if total > diff:
            total = diff
            final_num1 = nums[num_idx1]
            final_num2 = nums[num_idx2]

    if added_lst == []:
        return ()

    else:
        return (final_num1, final_num2)
