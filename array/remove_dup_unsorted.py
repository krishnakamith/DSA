"""Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]
Explanation: 2 and 1 have more than 1 occurence.
Input: arr[] = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
Explanation: There is no duplicate element.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)"""


#User function Template for python3



def removeDuplicate(self, arr):
    return list(dict.fromkeys(arr))



#my_solution
class Solution:
    def removeDuplicate(self, arr):
        map = {}
        for i in arr:
            map.update({i:None})
                
        a = []
        for i in map:
            a.append(i)
                
                
        return a
    
    