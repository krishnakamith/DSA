"""Given a string s, reverse the string without reversing its individual words. Words are separated by spaces.

Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.

Examples :

Input: s = " i like this program very much "
Output: "much very program this like i"
Explanation: After removing extra spaces and reversing the whole string (not individual words), the input string becomes "much very program this like i". 
Input: s = " pqr mno "
Output: "mno pqr"
Explanation: After removing extra spaces and reversing the whole string, the input string becomes "mno pqr". 
Input: s = " a "
Output: "a"
Explanation: The input string contains only one word with extra spaces around it. After removing the extra spaces, the output is "a".Constraints:"""
class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        str= ""
        s_list = s.strip().split()
        
        for i in s_list[:0:-1]:
            str = str + i + " "
        str += s_list[0]
        return str