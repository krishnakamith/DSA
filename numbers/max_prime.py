"""
Given a number n, your task is to find the largest prime factor of n.

Examples:

Input: n = 5
Output: 5
Explanation: The prime factorization of 5 is just 5. Therefore, the largest prime factor is 5.
Input: n = 24
Output: 3
Explanation: The prime factorization of 24 is 23×3. Among the prime factors (2, 3), the largest is 3.
Input: n = 13195
Output: 29
Explanation: The prime factorization of 13195 is 5×7×13×29. The largest prime factor is 29.
Constraints:
2 <= n <= 109

"""


class Solution:
    def largestPrimeFactor(self, n):
        while n%2 == 0:
            max_prime = 2
            n = n // 2
            
        for i in range(3, int(n**0.5)+1, 2):
            while n%i == 0:
                max_prime = i
                n = n // i
                
        if n>2:
            max_prime = n
            
        return max_prime
        
        