class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        if len(s) != len(t):
            return False
        freq1, freq2 = {}, {}
        for c1 in s:
            if c1 in freq1:
                freq1[c1] += 1
            else:
                freq1[c1] = 1
        for c2 in t:
            if c2 in freq2:
                freq2[c2] += 1
            else:
                freq2[c2] = 1
        return freq1 == freq2
        