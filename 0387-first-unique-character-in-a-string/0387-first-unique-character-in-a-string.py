class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m={}
        c=0
        f=False
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]]+=1
            else:
                m[s[i]]=1
        for i in range(len(s)):
            if m[s[i]]==1:
                return i

        return -1

                


        