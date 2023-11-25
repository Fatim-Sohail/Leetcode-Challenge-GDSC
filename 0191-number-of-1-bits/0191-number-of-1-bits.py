class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = binary.count('1')
        return count
    print (count)        