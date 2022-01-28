"""
Given two strings s and t, find the shortest substring of s that contains
all characters of t.
"""
from collections import Counter

# helper code
def contains_all(freq1, freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True


# Brute Force Approach
# Time Complexity: O(n^3)
# Space Complexity: O(n + m)
def bfs_min_window(s, t):
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""
    freqt = Counter(t)
    shortest = " "*(n+1)
    for length in range(1, n+1):
        for i in range(n-length+1):
            sub = s[i:i+length]
            freqs = Counter(sub)
            if contains_all(freqs, freqt) and length < len(shortest):
                shortest = sub
    return shortest if len(shortest) <= n else ""

# another approach
# Time Complexity: O(n^2)
# Space Complexity: O(n + m)
def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n+1
    for length in range(1, n+1):
        freqs = Counter()
        satisfied = 0
        for ch in s[:length]:
            freqs[ch] += 1
            if ch in freqt and freqs[ch] == freqt[ch]:
                satisfied += 1
        if satisfied == len(freqt) and length < end-start:
            start, end = 0, length
        for i in range(1, n-length+1):
            freqs[s[i+length-1]] += 1
            if s[i+length-1] in freqt and freqs[s[i+length-1]] == freqt[s[i+length-1]]:
                satisfied += 1
            if s[i-1] in freqt and freqs[s[i-1]] == freqt[s[i-1]]:
                satisfied -= 1
            freqs[s[i-1]] -= 1
            if satisfied == len(freqt) and length < end-start:
                start, end = i, i+length
    return s[start:end] if end-start <= n else ""

# best approach
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def best_min_window(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n
    satisfied = 0
    freqs = Counter()
    left = 0
    for right in range(n):
        freqs[s[right]] += 1
        if s[right] in freqt and freqs[s[right]] == freqt[s[right]]:
            satisfied += 1
        if satisfied == len(freqt):
            while s[left] not in freqt or freqs[s[left]] > freqt[s[left]]:
                freqs[s[left]] -= 1
                left += 1
            if right-left+1 < end-start+1:
                start, end = left, right
    return s[start:end+1] if end-start+1 <= n else ""

# driver code
if __name__ == '__main__':
    s = "ADCFEBECEABEBADFCDFCBFCBEAD"
    t = "ABCA"
    bfs_result = bfs_min_window(s, t)
    result = min_window(s, t)
    best_result = best_min_window(s, t)
    print(f"The result using Bruth Force Approach: {bfs_result}")
    print(f"The result using Bruth Force Approach: {result}")
    print(f"The result using Bruth Force Approach: {best_result}")
