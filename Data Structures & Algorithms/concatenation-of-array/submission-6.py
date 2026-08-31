class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # fin = []
        # for i in range(2):
        #     for num in nums:
        #         fin.append(num)
        # return fin

        n = len(nums)
        fin = [0] * (2*n)
        for i,num in enumerate(nums):
            fin[i] = fin[i+n] = num
        return fin

