class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev={}
        n=len(nums)
        for i in nums:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1
        for i in nums:
            if prev[i]>n/2:
                return i
