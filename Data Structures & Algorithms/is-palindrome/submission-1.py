class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s_new[::-1] == s_new
        
            
        