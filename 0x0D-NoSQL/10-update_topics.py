#!/usr/bin/env python3
"""Task 9. Change school topics"""


def update_topics(mongo_collection, name, topics):
    """List all documents"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
