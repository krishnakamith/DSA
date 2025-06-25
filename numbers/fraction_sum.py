"""
You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . Each test case contains four integers num1, den1, num2, den2 respectively .

Output Format:
For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes the sum of the two given fractions in reduced form.

Your Task:
Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function addFraction  which adds the two fractions and prints the resulting fraction. The function takes four arguments num1, den1, num2, den2 where num1, num2 denotes the numerators of two fractions and den1, den2 denotes their denominators.

Constraints:
1 <= T <= 100
1 <= den1,den2,num1,num2 <= 1000

Example:
Input
1
1 500 2 500
Output
3/500

Explanation:
In above test case 1/500+2/500=3/500
"""




#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
    #Code here
    if den1 == den2:
        num = num1 + num2
        print(f"{num}/{den1}")
        
    else:
        num1 = num1 * den2
        num2 = num2 * den1
        
        den = den1 * den2
        num = num1 + num2
        
        def hcf(a, b):
            while b != 0:
                a, b = b, a%b
            return a
            
        gcd = hcf(num, den)
        
        num = int(num/gcd)
        den = int(den/gcd)
        
        print(f"{num}/{den}")
        