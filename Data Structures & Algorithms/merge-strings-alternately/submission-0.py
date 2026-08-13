class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        x = min(l1,l2)
        fin = []


        for i in range(x):
            fin.append(word1[i])
            fin.append(word2[i])
        
        fin.append(word1[i+1:l1])
        fin.append(word2[i+1:l2])
        
        res = ''.join(fin)
        return res

        