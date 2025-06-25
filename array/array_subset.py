#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        map_a = {}
        for i in a:
            if i in map_a:
                map_a[i] += 1
            else:
                map_a[i] = 1
                
        for i in b:
            if i in map_a:
                map_a[i] -= 1
                if map_a[i] != -1:
                    bool = True
                else:
                    return False
            else:
                return False
                    
        return bool
    