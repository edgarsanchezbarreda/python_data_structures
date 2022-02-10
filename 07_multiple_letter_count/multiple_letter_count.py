def multiple_letter_count(phrase):
    letters_dict = {}
    for char in phrase:
        if char not in letters_dict.keys():
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1
        
    return letters_dict
        
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}    

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """