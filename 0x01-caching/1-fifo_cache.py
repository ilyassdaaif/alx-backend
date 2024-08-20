#!/usr/bin/env python3
"""
1-fifo_cache.py
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
