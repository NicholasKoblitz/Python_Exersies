def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {}
    count = 1
    for letter in phrase.lower():
        if letter in 'aeiou' and letter not in vowels:
            vowels.update({letter: 1})
        elif letter in 'aeiou' and letter in vowels:
            vowels[letter] += 1
    return vowels
