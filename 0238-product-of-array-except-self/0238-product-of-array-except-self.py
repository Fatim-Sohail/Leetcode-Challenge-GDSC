class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        pp = 1
        for i in range(n):
            answer[i] *= pp
            pp *= nums[i]
    
        sp = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= sp
            sp *= nums[i]
    
        return answer
