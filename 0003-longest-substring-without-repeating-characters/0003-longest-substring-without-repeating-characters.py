class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the index of each character
        char_index = {}
        
        # Initialize pointers for the sliding window
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            # If the character is already in the dictionary and its index is after the start pointer
            if s[end] in char_index and char_index[s[end]] >= start:
                # Move the start pointer to the next index after the repeating character
                start = char_index[s[end]] + 1
            
            # Update the index of the current character in the dictionary
            char_index[s[end]] = end
            
            # Update the max length
            max_length = max(max_length, end - start + 1)
        
        return max_length
