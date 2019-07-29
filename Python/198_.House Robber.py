'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


class Solution(object):
    def rob(self, nums):
        if not nums :
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i] = max(max(nums[i],nums[i-1]),nums[i-2]+nums[i])
        return nums[len(nums)- 1]
        

        
    def rob_2(self, nums):
        pre_one,pre_two = 0,0
        rob = 0 
        array =[]
        for n in nums:
            rob = max(pre_one,pre_two + n)
            array.append(rob)
            pre_two = pre_one
            pre_one =rob
        return rob
        
        
sol = Solution()
assert sol.rob_2([1,2,3,1]) == 4
assert sol.rob_2([2,7,9,3,1]) == 12
assert sol.rob([2,7,9,3,1]) == 12

