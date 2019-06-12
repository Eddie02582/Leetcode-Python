'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
            
        while n>1:
            if n % 3!= 0:
                return False
            n = n /3
        
        return True
        
    def isPowerOfTwo_log(self, n):  
        from  math import log   
        return n > 0 and int(log(n)/log(3))== round(log(n)/log(3),10)   