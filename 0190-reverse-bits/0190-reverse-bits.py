class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)
        reversed_str = binary_str[::-1]
        reversed_int = int(reversed_str, 2)
        return reversed_int
        