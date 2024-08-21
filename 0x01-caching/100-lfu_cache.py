#!/usr/bin/python3
"""
100-lfu_cache.py
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.keys_freq = {}
        self.freq_keys = {}
        self.min_freq = 0

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.get(key)

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            to_discard = min(self.freq_keys.keys())
            key_to_discard = self.freq_keys[to_discard].pop(0)
            if not self.freq_keys[to_discard]:
                del self.freq_keys[to_discard]
            del self.keys_freq[key_to_discard]
            del self.cache_data[key_to_discard]
            print("DISCARD:", key_to_discard)

        self.cache_data[key] = item
        self.keys_freq[key] = 1
        if 1 not in self.freq_keys:
            self.freq_keys[1] = [key]
        else:
            self.freq_keys[1].append(key)
        self.min_freq = 1

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        freq = self.keys_freq[key]
        self.keys_freq[key] = freq + 1
        self.freq_keys[freq].remove(key)
        if not self.freq_keys[freq]:
            del self.freq_keys[freq]
            self.min_freq = min(self.freq_keys.keys()) if self.freq_keys else 0
        if freq + 1 not in self.freq_keys:
            self.freq_keys[freq + 1] = [key]
        else:
            self.freq_keys[freq + 1].append(key)
        return self.cache_data[key]
