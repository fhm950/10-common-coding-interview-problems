"""
With the range of numbers from 1 to n inclusive, we can make n! permutations.
By labeling them in order starting from 1, you are asked to return the kth permutaiton.
"""

import itertools

# Brute-Force Search
# Time Complexity: O(n * n!)
def bfs_kth_permutation(n, k) -> str:
    permutations = list(itertools.permutations(range(1, n+1)))
    return ''.join(map(str, permutations[k-1]))


# Depth First Search
# Time Complexity: O(n^2)
def dfs_kth_permutation(n, k) -> str:
    permutation = []
    unused = list(range(1, n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k -= 1
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1
        k %= part_length
    return ''.join(map(str, permutation))

if __name__ == '__main__':
    n = 3
    k = 3
    bfs_result = bfs_kth_permutation(n, k)
    dfs_result = dfs_kth_permutation(n, k)
    print(f"The kth permutation by Brute-Force Search: {bfs_result}")
    print(f"The kth permutation by Brute-Force Search: {dfs_result}")