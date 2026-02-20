from concurrent.futures import ProcessPoolExecutor

def square(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return n * n


def parallel_square(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))

    return results