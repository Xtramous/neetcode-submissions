class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        fin = []
        for i in range(2):
            for num in nums:
                fin.append(num)
        return fin        