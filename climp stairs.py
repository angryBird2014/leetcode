class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = [1] * (n+1)
        for i in range(1,n+1):
            if i == 1:
                data[1] = 1
            elif i ==2:
                data[2] = 2
            else:
                data[i] = data[i-1] + data[i-2]
        return data[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(3))