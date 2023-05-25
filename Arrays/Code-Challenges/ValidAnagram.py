"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        # we can instantly check if its not a valid anagram if the lengths don't match
        if len(s) != len(t):
            return False
        # Keep track of both words count of letters with hashmaps
        countS = {}
        countT = {}

        # Because they are both the same length we can loop through them at the same time
        for i in range(len(s)):
            # For each time a letter appears add 1 to the value at the key in the hashmap which is the letter
            # the countS.get part is getting the value at the key if it exists and if it doesn't create the key and the default value will be 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # After the loop check if the counts are equal and return the boolean
        return countS == countT
        # Time Complexity: o(n) because we need to loop through each word completely
        # Space Complexity: o(n) because at worst we need to fill the hashmap at the length of the word assuming that each letter is unique
output = Solution()

print(output.isAnagram("anagram", "nagaram"))
print(output.isAnagram("rat","car"))
