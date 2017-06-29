class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)-1
        tmp_index = length
        while length >= 0 and s[length] == ' ':
            length -= 1
        actual_length = length
        if length >= 0:
            while length >= 0 and s[length] != ' ':
                length -= 1
                tmp_index = length
            return actual_length - tmp_index
        else:
            return 0



if __name__ == '__main__':
    s = Solution()
    str = 'ab '
    print(s.lengthOfLastWord(str))
