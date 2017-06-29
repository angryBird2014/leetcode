import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        if x < 0:
            return x
        else:
            for i in range(x//2+1):
                if i * i == x:
                    return i
                elif i * i < x and (i+1) *(i+1) > x:
                    return i
                elif (i+1) * (i+1) == x:
                    return i+1

        '''
        left = 0
        right = x // 2 +1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == '__main__':
    sol = Solution()

    print(sol.mySqrt(2))