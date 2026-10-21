class Solution:
    def isPalindrome(self, s: str) -> bool:
        regax = "[A-Za-z0-9]"
        sub = re.sub(r"[^A-Za-z0-9]+", "", s).lower()
        i = 0
        j = len(sub) - 1
        if len(sub) <= 1:
            return True
        while True:
            if sub[i] != sub[j]:
                return False
            i = i + 1
            j = j - 1
            if i >= j:
                break
        return True
            