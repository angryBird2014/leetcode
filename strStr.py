class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_length = len(haystack)
        needle_length = len(needle)
        i = 0
        if haystack_length==0 and needle_length == 0 :
            return 0
        else:
            if haystack_length < needle_length :
                return -1
            else:
                while i <= haystack_length - needle_length:
                    j = 0
                    while j < needle_length and needle[j] == haystack[i+j]:
                        j += 1
                    if j == needle_length:
                        return i
                    else:
                        i += 1
                return -1

if __name__ == '__main__':
    s = Solution()
    str = "123"
    value = "123"
    print(s.strStr(str,value))
