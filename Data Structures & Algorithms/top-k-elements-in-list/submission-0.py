class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get the freq of each element using counter
        # the key will be elements and value would be freq
        # create another dict with value,key
        # pick the top k
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        new_freq = []

        for i,val in freq.items():
            new_freq.append([val,i])
        new_freq.sort()

        fin = []

        while len(fin) < k:
            fin.append(new_freq.pop()[1])
        return fin



        