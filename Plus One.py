class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        digits_inverse = digits[::-1]
        jinwei = 0
        i = 0
        while i < length:
            if i == 0:
                if digits_inverse[i] + 1 >=10:
                    jinwei =1
                    digits_inverse[i] = digits_inverse[i]+1-10
                    if length == 1:
                        digits_inverse.insert(i+1,1)
                        return digits_inverse[::-1]
                else:
                    digits_inverse[i] = digits_inverse[i]+1
                    jinwei = 0
                    if length == 1:
                        return digits_inverse[::-1]
                i += 1
            elif i < length-1:
                if digits_inverse[i]+jinwei>=10:
                    digits_inverse[i] = digits_inverse[i]+jinwei-10
                    jinwei = 1
                else:
                    digits_inverse[i] = digits_inverse[i]+jinwei
                    jinwei = 0
                i += 1
            else:
                if digits_inverse[i] +jinwei>=10:
                    digits_inverse[i] = digits_inverse[i]+jinwei -10
                    jinwei = 1
                    digits_inverse.insert(i+1,1)
                else:
                    digits_inverse[i] = digits_inverse[i] + jinwei
                    jinwei = 0
                i += 1
        return digits_inverse[::-1]

if __name__ == '__main__':
    s = Solution()
    number = [1]
    print(s.plusOne(number))

