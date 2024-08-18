#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary with the hypermedia pagination information."""
        assert isinstance(index, int) and index in self.__indexed_dataset

        data = []
        current_index = index
        dataset_size = len(self.__indexed_dataset)

        for _ in range(page_size):
            while current_index not in self.__indexed_dataset and current_index < dataset_size:
                current_index += 1
            if current_index < dataset_size:
                data.append(self.__indexed_dataset[current_index])
                current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }

def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for pagination"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
