"""
Count Numbers in Range
Difficulty: MediumAccuracy: 28.44%Submissions: 9K+Points: 4Average Time: 20m
Given two positive integers L and R, return count of numbers having exactly 3 divisors from L to R inclusive.

 

Example 1:

Input:
L = 1, R = 10
Output:
2
Explanation:
4 and 9 are two numbers between 1 and 10
and have exactly 3 divisors.
Example 2:

Input:
L = 2, R = 5
Output:
1
Explanation:
4 is the only number between 2 and 5
and have exactly 3 divisors.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function count3DivNums() which takes 2 Integers L, and R as input and returns the count of numbers between L and R having exacly 3 divisors.

 

Expected Time Complexity: O(sqrt(R)*log(R))
Expected Auxiliary Space: O(sqrt(R))

 

Constraints:
1 <= L <= R <= 109
"""


#my logic - needs to be optimized

class Solution:
    def count3DivNums(self, L, R):
        # code here
        def factorCount(n):
            factorcount = 0
            root = int(n ** 0.5) + 1
            for i in range(1,root):
                if n%i == 0:
                    if (i == n // i):
                        factorcount += 1
                    else:
                        factorcount += 2
            return factorcount
            
        count = 0
        for i in range(L, R+1):
            if factorCount(i) == 3:
                count += 1
        return count
    
#hint: Only perfect squares of prime numbers have exactly 3 divisors
#e.g., 4 (2²), 9 (3²), 25 (5²)


class Solution:
    def count3DivNums(self, L, R):
        # code here
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n%i == 0:
                    return False
            return True
                
            
        count = 0  
        start = int(L ** 0.5)
        end = int(R ** 0.5)
        for root in range(start, end+1):
            square = root*root
            if L <= square <= R and isPrime(root):
                count+=1
                
        return count