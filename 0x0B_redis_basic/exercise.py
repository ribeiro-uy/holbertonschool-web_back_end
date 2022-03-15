#!/usr/bin/env python3
"""exercise"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
TYPES = Union[str, bytes, int, float]


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
