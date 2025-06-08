class Solution:
    def firstNonRepeating(self, arr):
        h = {}
        for i in arr:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in arr:
            if h[i] == 1:
                return i
        return 0
      