class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        left=0
        
        for i in s:
            if i.isalnum():
                ans+=i
        right=len(ans)-1
        while left<right:
            if ans[left]!=ans[right]:
                return False
            left+=1
            right-=1
        return True
            
        

