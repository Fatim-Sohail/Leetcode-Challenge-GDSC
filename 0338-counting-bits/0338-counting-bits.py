class Solution:
    def countBits(self, n: int) -> List[int]:
         # Initialize the result array with zeros
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # No. of 1's in the binary representation of i = No. of 1's in i // 2
            ans[i] = ans[i // 2] + (i % 2)

        return ans