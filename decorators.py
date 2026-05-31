import sys

def WindowsOnly(func):
    def wrapper(*args, **kwargs):
        if sys.platform == "win32":
            return func(*args, **kwargs)
        else:
            print(f"Caution: your system dont supported function: {func.__name__}")
            return None
    return wrapper