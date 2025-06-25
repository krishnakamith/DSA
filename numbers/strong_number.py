"""Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number N, the task is to check if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0.

 

Example 1:

Input:
N = 145
Output:
1
Explanation:
1! + 4! + 5! = 145 So, 145 is a Strong
Number and therefore the Output 1.
Example 2:

Input:
N = 14
Output:
0
Explanation:
1! + 4! = 25 So, 14 isn't a Strong
Number and therefore the Output "NO"."""

#User function Template for python3

class Solution:
    def isStrong(self, N):
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
                
        fact = 0
        for i in str(N):
            n = int(i)
            fact += factorial(n)
        
        if fact == N:
            return 1
        return 0