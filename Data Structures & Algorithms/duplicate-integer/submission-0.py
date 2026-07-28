class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev={}
        for i in nums:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1
        for i in nums:
            if prev[i]>1:
                return True
            
        return False