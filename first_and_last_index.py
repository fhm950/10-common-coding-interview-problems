"""
Find the first and last index of a target value from a sorted array of integers
Given a sorted array of integers arr and an integer target,
find the index of the first and last position of target in arr.
In the target can't be found in arr, return [-1, -1]
"""
from typing import List

def find_start(arr, target) -> int:
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_end(arr, target) -> int:
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def first_and_last(arr, target) -> List:
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]


if __name__ == '__main__':
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5
    result = first_and_last(arr, target)
    print(f'The first index is {result[0]} and the last index is {result[1]}')