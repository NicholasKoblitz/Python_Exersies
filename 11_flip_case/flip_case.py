def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_phrase = []

    for letter in phrase:
        if to_swap.islower():
            if letter.islower() and letter == to_swap:
                new_phrase.append(letter.upper())
            elif letter.isupper() and letter.lower() == to_swap:
                new_phrase.append(letter.lower())
            else:
                new_phrase.append(letter)
        elif to_swap.isupper():
            if letter.isupper() and letter == to_swap:
                new_phrase.append(letter.lower())
            elif letter.islower() and letter.upper() == to_swap:
                new_phrase.append(letter.upper())
            else:
                new_phrase.append(letter)

    phrase = ''
    phrase = phrase.join(new_phrase)

    return phrase
