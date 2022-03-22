#!/usr/bin/env python3
"""Task 11. Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """List all documents"""
    return mongo_collection.find(
        {'topics': topic},
    )
