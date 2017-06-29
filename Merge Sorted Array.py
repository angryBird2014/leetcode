class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0  and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            elif nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        print(n)

if __name__ == '__main__':
    nums1 = [1,2,3,4,-1]
    m = 4
    nums2 = [3]
    n = 1
    sol = Solution()
    sol.merge(nums1,m,nums2,n)





