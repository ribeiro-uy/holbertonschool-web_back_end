#!/usr/bin/env python3
"""exercise"""
import redis
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4
TYPES = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """Count how many times methods are called"""
    @wraps(method)
    def timesCalled(self, *args, **kwds):
        """Increments method call counter"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return timesCalled


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs"""
    @wraps(method)
    def history(self, *args, **kwds):
        """Increments history call method"""
        inputs = method.__qualname__ + ":inputs"
        outputs = method.__qualname__ + ":outputs"
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(outputs, output)
        return output
    return history


def replay(method: Callable):
    """Display history of calls"""
    qualname = method.__qualname__
    redis = method.__self__._redis
    calls = redis.llen(qualname + ":inputs")
    inputs = redis.lrange(qualname + ":inputs", 0, -1)
    outputs = redis.lrange(qualname + ":outputs", 0, -1)
    print(f'{qualname} was called {calls} times:')

    for input, output in zip(inputs, outputs):
        key = input.decode("utf-8")
        value = output.decode("utf-8")
        print(f'{qualname}(*{key})' + f' -> {value}')


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: TYPES) -> str:
        """Store the input data in Redis"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> TYPES:
        """Get key from redis"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: bytes) -> str:
        """Parametrize Cache.get as string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get as int"""
        return self.get(key, int)
