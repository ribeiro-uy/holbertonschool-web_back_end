#!/usr/bin/env python3
"""exercise"""
import redis
from uuid import uuid4
from typing import Union

Types = Union[str, bytes, int, float]


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Types) -> str:
        """Store the input data in Redis"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
