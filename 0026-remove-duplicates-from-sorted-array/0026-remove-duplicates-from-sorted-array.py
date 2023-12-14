class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow_ptr = 0

        # Iterate through the array with fast pointer
        for fast_ptr in range(1, len(nums)):
            # If the current element is different from the previous one, update slow pointer
            if nums[fast_ptr] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[fast_ptr]

        # The unique elements are stored in the beginning of the array up to slow pointer
        # The length of the array with unique elements is (slow_ptr + 1)
        return slow_ptr + 1
