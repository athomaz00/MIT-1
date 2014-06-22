def mapList(f, seq):
    """
    Maps a function over a list.

    Args:
        f: a function to call
        seq: the sequence to iterate over
    """
    return [f(x) for x in seq]

sum(map(abs, [1, 2, 3, -4]))

def mapSquare(f, seq):
    return [[f(x, y) for y in seq] for x in seq]