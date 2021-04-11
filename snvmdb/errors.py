class DatabaseNotFoundError(Exception):
    """
    Raised when database file wasn't found.
    """
    pass


class NotListError(Exception):
    """
    Raised when trying using list function on other values
    """
    pass


class NotHashError(Exception):
    """
    Raised when trying using hash function on other values
    """
    pass

class NotSecondActionError(Exception):
    """
    Raised when calling .completely_destroy() as first action.
    """
    pass
