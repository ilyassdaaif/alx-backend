#!/usr/bin/env python3
"""
0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
