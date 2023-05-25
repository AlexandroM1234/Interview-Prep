"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        # have a hashmap to keep track of the compliments we need and their index
        compliments = {}
        # loop through the list
        for i in range(len(nums)):
            # calculate the compliment we need to find
            comp = target - nums[i]
            # if the compliment is already in the list return the value at that key in the hashmap and return the current index we are on
            if comp in compliments:
                return [compliments[comp], i]
            else:
                # otherwise add the number we are on to the list of compliments along with its index
                compliments[nums[i]] = i
        # Time Complexity: o(n) at worst we need to loop through the whole list to find the compliment
        # Space Complexity: o(n) at worse we need to fill the hashmap with every number until the last one assuming that there is always a solution
output = Solution()

print(output.twoSum([1,2,3,4,5], 5))
print(output.twoSum([1,2,3,4,5,6,7,],7))
