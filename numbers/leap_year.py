"""You are given an Integer n. Return true if It is a Leap 
Year otherwise return false."""




#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        return n%400 == 0 or (n%100 != 0 and n%4 == 0)