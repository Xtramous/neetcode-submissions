class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #in place replacement

        nums_copy = nums1[:m]
        index = 0
        i = j = 0

        while index < m+n:
            if j >= n or (i < m and nums_copy[i] <= nums2[j]):
                nums1[index] = nums_copy[i]
                i+=1
            else:
                nums1[index] = nums2[j]
                j+=1
            index+=1
        