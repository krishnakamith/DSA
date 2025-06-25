"""Find the first occurrence of the string pat in the string txt. The function returns an integer denoting the first occurrence of the string pat in txt (0-based indexing).

Note: You are not allowed to use the inbuilt function. If there is no occurrence then return -1.

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: Fr is not present in the string GeeksForGeeks as substring.
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: For is present as substring in GeeksForGeeks from index 5 (0 based indexing).


"""

#Function to locate the occurrence of the string x in the string s.
class Solution:
    def firstOccurence(self,txt,pat):
        #code here
    
        for x in range(len(txt)):
            if txt[x:x+len(pat)] == pat:
                return x
            
            
        return -1
                
                    
                    