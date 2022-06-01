from .cart import Cart

def cart(request):
    """
    this function will be placed-
    at the bottom of the templates -> 'context_processors'.
    Therefore, the key -> cart will be available globaly.
    """
    return {'cart': Cart(request)}