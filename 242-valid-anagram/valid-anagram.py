class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

            if s[i] not in hashmapS:
                hashmapS[s[i]] = 1
            else:
                hashmapS[s[i]] = hashmapS[s[i]] + 1 

        for char in hashmapS:
            if hashmapS[char] != hashmapT.get(char, 0):
                return False
        
        return True
        