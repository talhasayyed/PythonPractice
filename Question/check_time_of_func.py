from typing import Callable 
import time

from febonacci_optimised import febonacci
from febonacci_recursion import fibonacci_recursive

def time_function(func: Callable [[int], int], n: int) -> None:
    start_time: float = time.perf_counter()
    result: int = func(n)
    end_time: float = time.perf_counter()
    # Print information
    print(f'{func.___name__}({n})={result}')
    print(f'Total time: {end_time - start_time:.4f}s')


# print febonacci_recursive time
print(time_function(func: febonacci_recursive, n:10))

# print febonacci optimised time
print(time_function(func: febonacci, n:10))
