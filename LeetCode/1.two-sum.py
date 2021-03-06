#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (43.07%)
# Total Accepted:    1.7M
# Total Submissions: 3.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      nums_table = {}
      for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in nums_table.keys():
          return [nums_table[complement], i]
        else:
          nums_table[nums[i]] = i



