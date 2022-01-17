"""
checking if two strings are anagram.
Two strings are anagrams if they're made of the same characters with the same frequencies
We need to create two separate frequencies which replicate the characters of each strings.
Both the frequencies are same then two strings are anagrams.
"""

def are_anagrams(str_1, str_2) -> bool:
    if len(str_1) != len(str_2):
        return False
    freq_1 = {}
    freq_2 = {}
    
    for ch in str_1:
        if ch in freq_1:
            freq_1[ch] += 1
        else:
            freq_1[ch] = 1
    
    for ch in str_2:
        if ch in freq_2:
            freq_2[ch] += 1
        else:
            freq_2[ch] = 1
    
    for key in freq_1:
        if key not in freq_2 or freq_1[key] != freq_2[key]:
            return False
    return True


if __name__ == '__main__':
    test_1 = "danger"
    test_2 = "garden"
    result = are_anagrams(test_1, test_2)
    print(f"{test_1} and {test_2} are anagrams: {result}")

