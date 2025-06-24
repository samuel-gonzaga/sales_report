import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱️ Tempo total: {time.time() - start:.2f}s")
        return result
    return wrapper
