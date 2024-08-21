#!/usr/bin/env python3
"""
3-lru_cache.py
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_order.remove(key)
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.keys_order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.keys_order.remove(key)
        self.keys_order.append(key)
        return self.cache_data[key]
