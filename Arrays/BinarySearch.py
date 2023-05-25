
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution:
    def binarySearch(self, nums:list[int], target:int)->int:
        # have 2 variables keeping the left and right indicies 
        l = 0
        r = len(nums) - 1

        # keeping looping until the l = r 
        while l <= r:
            # calculate the middle of the list
            mid = (l + r) // 2
            # if the number is at the middle return the index
            if nums[mid] == target:
                return mid
            # if the number at the middle is larger than the target make the right most index the middle - 1
            elif nums[mid] > target:
                r = mid - 1
            # then if the middle value is less than the target make the left most index the middle + 1
            # the +1 -1 are needed so we don't recount values
            else:
                l = mid + 1
        # if the target isn't found return -1
        return -1 
        # Time Complexity: o(log n) because each time we calculate we are dividing the number of computations we need to do by half every time
        # Space Complexity: o(1) because we aren't using any external data structure to store values as the size of the input list grows
        # IMPORTANT: VALUES HAVE TO BE SORTED

output = Solution()
print(output.binarySearch([1,2,3,4,5,6,7,8],6))
print(output.binarySearch([1,2,3,4,5,6,7,8],10))

