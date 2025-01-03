"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):

    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def get_random_ingredients_B(kind=None):
    """
    Return a list of random ingredients as strings.

    Parameters
    ----------
    kind : list[str] or None, optional
        Specifies the kind of ingredients to return. The default is None, which means all kinds are included.

    Returns
    -------
    list[str]
        A list of ingredient names.

    Raises
    ------
    InvalidKindError
        If the kind is invalid.
    """
    return ["shells", "gorgonzola", "parsley"]
