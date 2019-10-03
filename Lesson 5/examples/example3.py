def max(*args):
    is_iterable = isinstance(args[0], (list, tuple, set, frozenset, dict))
    if len(args) == 1 and is_iterable:
        args = args[0]

    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i

    return m
