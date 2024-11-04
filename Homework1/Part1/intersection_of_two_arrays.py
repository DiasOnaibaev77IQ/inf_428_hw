class Solution(object):
    def findLengthOfLCIS(self, nums):
        lengthOfArray = len(nums)
        count = 1
        maximum = count
        for i in range(0, lengthOfArray - 1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                count = 1
            
            maximum = max(count, maximum)
        
        return maximum
