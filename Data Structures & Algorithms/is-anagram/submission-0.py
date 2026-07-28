class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prevS={}
        for i in s:
            if i in prevS:
                prevS[i]+=1
            else:
                prevS[i]=1
        prevT={}
        for i in t:
            if i in prevT:
                 prevT[i]+=1
            else:
                prevT[i]=1
        return  prevS==prevT
