# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
from collections import defaultdict

def isAnagram(s, t):
    refDict = defaultdict(int)
    for letter in s:
        refDict[letter]+=1
    checkDict = defaultdict(int)
    print(refDict)
    for t_letter in t:
        checkDict[t_letter]+=1
    return checkDict == refDict
# check = isAnagram("anagram", "nagaram")
# print(check)

def neetIsAnagram(s,t):
    if len(s) != len(t):
        return False
    # Creating two dictionaries
    countS, countT = {}, {}
    #Assume they are the same size at this point so can use the length
    for i in range(len(s)):
        # Get works by getting the key so for the first one it would be 'a' and 0 is the default value if the value does not exist
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    print(countS, countT)
    return countS == countT
check = neetIsAnagram("anagram", "nagaram")
print(check)