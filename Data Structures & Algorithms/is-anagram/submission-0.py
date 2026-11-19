class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower().replace(" ", "")
        t = t.lower().replace(" ", "")
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)