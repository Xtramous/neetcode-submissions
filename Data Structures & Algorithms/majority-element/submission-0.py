class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        l = len(nums)

        for i,val in freq.items():
            if val >= l//2:
                return i
        
        