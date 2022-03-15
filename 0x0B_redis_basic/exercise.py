#!/usr/bin/env python3
"""exercise"""
import redis
from uuid import uuid4


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """Store the input data in Redis"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
