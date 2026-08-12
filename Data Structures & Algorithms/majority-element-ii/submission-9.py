from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        fin = Counter(nums)
        res = []
        for i,val in fin.items():
            if val > len(nums)//3:
                res.append(i)
        return res
                

        