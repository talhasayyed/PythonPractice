import functools

def dummy_data(data, *, verbose=False):
    """
    Decorator to replace function logic with dummy data.

    Args:
        data: The dummy data to return instead of running the function.
        verbose (bool): If True, prints a message when the dummy data is used.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if verbose:
                print(f"[dummy_data] Returning dummy data for {func.__name__}")
            return data
        return wrapper
    return decorator

# Example usecase 1
@dummy_data(data={"status": "success", "data": [1, 2, 3]}, verbose=True)
def fetch_api_data():
    # In reality, this would call an API
    raise Exception("You should not see this!")  # Just to show it won’t be run

result = fetch_api_data()
print(result)  # -> {'status': 'success', 'data': [1, 2, 3]}

