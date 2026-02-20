from concurrent.futures import ProcessPoolExecutor
import math
import time
import sys

sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    print(f"Computing factorial of {n}")
    time.sleep(1)
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [50000, 60000, 70000]

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_factorial, numbers)

    for result in results:
        print("Result length:", len(str(result)))