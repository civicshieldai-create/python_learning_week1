import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result= func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start: 4f} seconds")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(1)
    return "Done!"

print(slow_function())
