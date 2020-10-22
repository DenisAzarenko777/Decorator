import time
import datetime
from debug import decorator

@decorator
def some_function(a, b):
    result = a * b
    return result

some_function(10,8)
