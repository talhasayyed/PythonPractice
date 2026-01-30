import time

# create a decorator for time measurement
def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@time_measurement
def test():
    time.sleep(3)

if __name__=='__main__':
    test()
