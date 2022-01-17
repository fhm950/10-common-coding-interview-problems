"""
Finding the Kth largest integer.
Given an array of integers arr and an integer k,
find the kth largest element
"""

import heapq


def kth_largest(arr, k) -> int:
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


if __name__ == '__main__':
    arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    k = 4
    result = kth_largest(arr, k)
    print(f'The {k}th largest element is {result}')