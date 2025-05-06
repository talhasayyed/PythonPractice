# If you want to get fancy and allow data to be a callable (like a lambda or factory), you can do:

def dummy_data(data_or_callable, *, verbose=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if verbose:
                print(f"[dummy_data] Returning dummy data for {func.__name__}")
            return data_or_callable() if callable(data_or_callable) else data_or_callable
        return wrapper
    return decorator


import random
@dummy_data(lambda: random.randint(1, 100), verbose=True)
def get_random_number():
    return 42  # ignored

print(get_random_number())  # -> random dummy number each time
