class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #numers is already sorted
        #res to hold the 1-indexed result
        res = []

        left,right = 0,len(numbers)-1

        while left < right:
            sum_2 = numbers[left] + numbers[right]

            if sum_2 < target:
                left +=1
            elif sum_2 > target:
                right -=1
            else:
                res.append(left+1)
                res.append(right+1)
                left+=1
                right-=1

        return res
        