def compact(lst):
    empty_lst = []
    for element in lst:
        if element:
            empty_lst.append(element)
    return empty_lst

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """