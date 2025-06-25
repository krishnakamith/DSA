class Solution:
    def isPrime(self, n):
        root = int(n ** 0.5)
        if n <= 1:
            return False
        for i in range(2, root + 1):
            if n % i == 0:
                return False
        return True