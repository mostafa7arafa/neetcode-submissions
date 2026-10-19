class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict(Counter(s))
        count_t = dict(Counter(t))
        return count_s == count_t

        