class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        for i, j in zip(word1 , word2):
            ans+=i+j
        ans+=word1[len(word2):]
        ans+=word2[len(word1):]
        return ans

