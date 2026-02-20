from multiprocessing import Process
import os

def task(name):
    print(f"Hello {name}")
    print(f"Process ID: {os.getpid()}")

if __name__ == "__main__":
    p1 = Process(target=task, args=("Talha",))
    p2 = Process(target=task, args=("World",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process finished")

# Output ---------------------
# Hello Talha
# Process ID: 204119
# Hello World
# Process ID: 204120
# Main process finished


# # Example Using Pool (Parallel Map)
# from multiprocessing import Pool

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     with Pool(4) as p:
#         result = p.map(square, [1, 2, 3, 4])
#         print(result)

# # Output
# # [1, 4, 9, 16]

"""
Important Concept: GIL (Global Interpreter Lock)
In CPython:
•	Only one thread executes Python bytecode at a time
•	So multithreading does NOT give true parallelism for CPU-bound tasks
That’s why:
✔ Use multithreading for:
•	API calls
•	Database calls
•	File reading/writing
•	Network operations
✔ Use multiprocessing for:
•	Heavy computation
•	Data processing
•	ML training
•	Image processing

"""

"""
Difference Between Multiprocessing and Multithreading

| Feature       | Multithreading                            | Multiprocessing                         |
| ------------- | ----------------------------------------- | --------------------------------------- |
| Definition    | Multiple threads in same process          | Multiple independent processes          |
| Memory        | Shared memory                             | Separate memory                         |
| Speed         | Lightweight                               | Heavyweight                             |
| Communication | Easy (shared vars)                        | Needs IPC (Queue, Pipe)                 |
| GIL Impact    | Affected by GIL                           | Not affected                            |
| Best For      | I/O-bound tasks                           | CPU-bound tasks                         |
| Crash Impact  | One thread crash may affect whole process | One process crash doesn't affect others |

"""