import threading

def square(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return n * n


def run_threads(numbers):
    results = []

    def worker(num):
        results.append(square(num))

    threads = []
    for n in numbers:
        t = threading.Thread(target=worker, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(results)