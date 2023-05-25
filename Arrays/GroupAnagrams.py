"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        # keeep a hashmap to keep track of the groups
        # the key will be the count of letters per word the value will be the words where they match up with the same key
        ans = {}

        # loop through the outer list
        for word in strs:
            # for each word in the list create a list of length 26 being the length of the alphabet then the indices being the corresponding letters
            count = [0] * 26
            for char in word:
                # for each letter in the word use the ord function to get the unicode integer the subtract that by "a" to get the index for our list of letters in the alphabet
                # ex "a" == 97 so a - a == 97 - 97 == 0 which is the 0th index in our list and so on for the rest of the letters
                # once we get an index for the letter we then add 1 for everytime it is used in the word
                count[ord(char) -  ord("a")] += 1
            # once we are out of the loop for the characters in a word we need to make the count a tuple so we can hash it as a key in our dictionary
            key = tuple(count)
            
            # then check if the key is in the hashtable if it is append the word at that key otherwise create a new key then the value would be an array with the word in it
            if key in ans:
                ans[key].append(word)
            else:
                ans[key] = [word]
        # afterwards we can output the hashtables values
        return ans.values()
        # Time Complexity: o(n) because we need to loop through all of the words in the list and then we loop through all the characters in the words but we are not looping through the outer list for every character we have so its really o(m*n) m being the average length of the words which simplifies to o(n)

        # Space Complexity: o(n) because at worst we need to create a key for every word in the list of strings and the values would be one word in each list
output = Solution()
print(output.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(output.groupAnagrams([""]))
print(output.groupAnagrams("a"))