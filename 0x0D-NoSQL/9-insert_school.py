#!/usr/bin/env python3
"""Task 9. Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a mongo collection based on kwargs"""
    if kwargs:
        x = mongo_collection.insert_one(kwargs)
        return x.inserted_id
