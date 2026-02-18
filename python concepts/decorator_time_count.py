import time
import logging

# logging.basicConfig(level=logging.INFO)

# Decorator using @
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        # logging.info(f'Execution of {func.__name__} took {execution_time:.2f} seconds')
        print(f'Execution of {func.__name__} took {execution_time:.2f} seconds')
        return result
    return wrapper  # Missing return statement for the wrapper function

@time_decorator
def test(seconds):  # Parameter name must be valid; corrected to "seconds"
    # Simulating function taking `seconds` time
    for i in range(seconds):
        time.sleep(1)
    return 'Test run complete'  # Fixed result assignment and return statement

# Example usage
if __name__ == "__main__":
    print(test(5))  # Corrected function call
