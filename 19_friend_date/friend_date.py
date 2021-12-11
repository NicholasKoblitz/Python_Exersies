def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    (a_name, a_age, a_hobbies) = a
    (b_name, b_age, b_hobbies) = b

    true_lst = []

    for item in a_hobbies:
        if item in b_hobbies:
            true_lst.append(True)
        else:
            true_lst.append(False)

    if True in true_lst:
        return True
    else:
        return False
