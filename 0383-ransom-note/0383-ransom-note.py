from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r=Counter(ransomNote)
        m=Counter(magazine)
        for a,b in enumerate(r):
            if(r[b]>m[b]):
                return False
        return True


        