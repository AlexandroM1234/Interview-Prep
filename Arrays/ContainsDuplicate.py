"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: list [int]) -> bool:
        # create a set to keep track of the unique values
        nonDups = set()

        # loop through the numbers in the list
        for num in nums:
            # if we reach a number that is in the set return true
            if num in nonDups:
                return True
            # otherwise keep adding numbers to the set
            nonDups.add(num)
        # if we reach the end of the end of the loop return False
        return False
        # Time Complexity: o(n) at worst we need to go through the entire list and there a no duplicates
        # Space Complexity: o(n) at worst we need to fill the set with all unique numbers
output = Solution()

print(output.containsDuplicate([1,2,3,4,4]))