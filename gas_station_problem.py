"""
Given a circular list of gas stations, where we can go from a station i to the
station i+1, and the last one goes back to the first one, find the index of the station from
where we start to be able to traverse all the stations and go back to the initial one without
running out of gas.
Note:
- We can only move forward
- The gas tank starts empty
- gas[i] represents the amount of gas at the station i
- cost[i] represents the cost to go from the station i to the next one
- the answer is guaranteed to be unique
- if the station we're searching for doesn't exist, return -1
"""

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def can_traverse(gas, cost, start) -> bool:
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True


def gas_station(gas, cost) -> int:
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1


# Ordinarry Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def gas_station(gas, cost) -> int:
    remaining = 0
    prev_remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            prev_remaining += remaining
            remaining = 0
    if candidate == len(gas) or remaining+prev_remaining < 0:
        return -1
    else:
        return candidate

if __name__ == '__main__':
    gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
    cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
    result = gas_station(gas, cost)
    print(f'The index of the station is {result}')

