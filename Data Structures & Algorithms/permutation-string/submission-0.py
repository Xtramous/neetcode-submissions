from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        if count_s1 == window:
            return True
        
        for i in range(len(s1),len(s2)):
            window[s2[i]] +=1
            last_char = s2[i-len(s1)]
            window[last_char] -=1

            if window == count_s1:
                return True
        return False
        

        