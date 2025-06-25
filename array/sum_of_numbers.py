"""
Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Examples:

Input: s = "1abc23"
Output: 24
Explanation: 1 and 23 are numbers in the string which is added to get the sum as 24.
"""

#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self, s):
        #code here
        num = ""
        sum = 0
        
        for i in s:
            if i.isdigit():
                num += i
            elif i.isalpha():
                if num != "":
                    n = int(num)
                    sum += n
                num = ""
                
        if num != "":
            n = int(num)
            sum += n
        
        
        return sum
               
        
