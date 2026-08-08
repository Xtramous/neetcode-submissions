class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # create a stack
        #start from the last element using enumerate i,num
        # pop if c
        cnt = 0
        for i,num in enumerate(nums):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt


        
        