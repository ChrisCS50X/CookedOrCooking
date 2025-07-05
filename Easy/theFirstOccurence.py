class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = ''
        found = False

        for i in range (len(haystack) + 1 - len(needle)):
            for j in range (len(needle)):
                ans += haystack[i+j]

                if (ans == needle):
                    found = True
                    break
            
            if (found == True):
                return i

            else:
                ans = ''

        return -1

        