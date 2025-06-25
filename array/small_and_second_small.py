"""
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second 
smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element
"""

#User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        #code here
        if len(arr) < 2:
            return -1, -1
            
        arr.sort()
        smallest = arr[0]
        
        for i in arr:
            if i > smallest:
                return smallest, i
            
        else:
            return -1, -1
        
        
    

