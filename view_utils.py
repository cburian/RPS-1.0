
def prt_delimiter(length, border: str = '-'):
    """Applies border to message - for important messages

    todo: make this into a decorator
    """
    print(border * length)
