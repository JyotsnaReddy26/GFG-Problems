#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        sqsum=0
        i=1
        while i<=number:
            sqsum+=i*i
            i+=1
        return sqsum