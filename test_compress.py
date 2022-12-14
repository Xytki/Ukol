import gzip


def test_gz_is_empty(fname):
    """ Test if gzip file fname is empty
        Return True if the uncompressed data in fname has zero length
        or if fname itself has zero length
        Raises OSError if fname has non-zero length and is not a gzip file
    """
    with gzip.open(fname, 'rb') as f:
        data = f.read(1)
    return len(data) == 0
