"""
Decorator is to wrap the input function in order to modify its behavior at call time
To use as decorator to make a function call threaded.
uses it to wrap the input function in order to modify its behavior at call time

Needs to import
from threading import Thread


eg : 
@start_new_thread
def function_name()
"""
def start_new_thread(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper
