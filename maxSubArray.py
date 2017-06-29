class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = 0
        maxSum = 0
        i = 0
        j = -1
        if all(v < 0 for v in nums):
            return max(nums)
        else:
            for index,value in enumerate(nums):
                if currentSum + value < value:
                    currentSum = value
                    i = index
                elif currentSum + value >= value:
                    currentSum += value
                    j += 1
                if currentSum > maxSum :
                    maxSum = currentSum
            return maxSum,i,j
if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
