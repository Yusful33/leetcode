# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.

 

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list) # mapping charCount to list of anagrams

    for s in strs:
        count = [0] * 26 # a...z
        for c in s:
            # taking the asky value (where c is a letter in the word) a - a = 0 but z - a = 25
            count[ord(c) - ord("a")] += 1
        # group all anagrams together
        # Need to change to tuple as keys cannot be list (need to be unique)
        res[tuple(count)].append(s)
    # print(res)
    return res.values()


test = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(test)