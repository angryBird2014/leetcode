class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while j >= 0 and i <= j:
            while j>=0 and nums[j] == val:
                j -= 1
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i




if __name__ == '__main__':
    s = Solution()
    nums =  [3,3,3,1,2,2,3,3,3,5,6,7,8,9,3,3]
    val = 3
    length = s.removeElement(nums,val)
    #print(length , " " , nums[-length:])
    print(length , " ",nums[:length])