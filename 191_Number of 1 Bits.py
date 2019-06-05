'''
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

'''




class Solution(object):
    def hammingWeight_format(self, n):
        return  format(n,'b').count('1')

    def hammingWeight(self, n):
        count=0
        for i in range (0,32):
            if n >> i & 1 == 1:
                count+=1
        return  count

    def hammingWeight(self, n):
        count=0
        while n :
            n,res=divmod(i, 2)        
            if res==1:
               count+=1
        return  count



sol =Solution()

assert sol.hammingWeight(5)=='2'


