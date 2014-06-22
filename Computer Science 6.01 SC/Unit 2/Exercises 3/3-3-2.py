def recursiveRef(seq, indexes):
    if indexes:
        return recursiveRef(seq[indexes[0]], indexes[1:])
    else:
        return seq

nested = [[[1, 2], 3], [4, [5, 6]], 7, [8, 9, 10]]