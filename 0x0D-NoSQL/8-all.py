#!/usr/bin/env python3
"""Task 8. List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """Lists all documents in a mongo collection    """
    cursor = mongo_collection.find({})
    return cursor
