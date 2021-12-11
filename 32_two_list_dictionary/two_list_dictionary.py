def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    collection = {}

    for key in keys:
        idx = keys.index(key)

        if values[idx] == values[-1]:
            collection.update({key: values[idx]})
            if keys[idx] != keys[-1]:
                collection.update({keys[idx + 1]: None})
            break
        else:
            collection.update({key: values[idx]})

    return collection
