class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        trangle = []
        for index in range(1,numRows+1):
            if index == 1:
                tmp = [1]
            elif index == 2:
                tmp = [1,1]
            else:
                tmp = [1] * index
                for index2 in range(1,index-1):
                    tmp[index2] = trangle[index-1-1][index2-1] + trangle[index-1-1][index2]
            trangle.append(tmp)
        print(trangle)
if __name__ == '__main__':
    sol = Solution()
    sol.generate(3)
