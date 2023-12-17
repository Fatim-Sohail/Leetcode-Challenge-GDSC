class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(left, right):
            count = 0
            # Expand outwards from the center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total_count = 0

        # Consider each character and its potential center
        for i in range(len(s)):
            # Count palindromes with odd length
            total_count += countPalindromes(i, i)
            # Count palindromes with even length
            total_count += countPalindromes(i, i + 1)

        return total_count

