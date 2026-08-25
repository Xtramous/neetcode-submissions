from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        for i,val in freq.items():
            if val == 1:
                return i

        