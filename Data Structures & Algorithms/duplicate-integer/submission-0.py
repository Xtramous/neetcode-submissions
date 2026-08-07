class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        for i,val in freq.items():
            if val > 1:
                return True
        return False
        