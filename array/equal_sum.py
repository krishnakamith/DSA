#o(n)
class Solution:
    def equilibrium(self,arr):
        n = len(arr)
        totalsum = sum(arr)
        leftsum = 0

        for i in range(n):
            rightsum = totalsum - leftsum - arr[i]
        if rightsum == leftsum:
            return "true"
        leftsum += arr[i]
    
        return "false"
        




#My solution: naive/bruteforce o(n^2)
class Solution:
    def equilibrium(self,arr):
        n = len(arr)
        if n == 1:
            return "true"
    	 
        for i in range(n):
            sum1 = sum(arr[:i])
            sum2 = sum(arr[i+1:])
            if sum1 == sum2:
                return "true"
    	        
        return "false"