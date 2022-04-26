import os

def listSum(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + listSum(nums[1:])
