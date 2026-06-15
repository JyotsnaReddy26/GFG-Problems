#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        original=n
        count=len(str(n))
        total=0
        while n>0:
            last_digit=n%10
            total+=last_digit**count
            n//=10
        
        if original==total:
            return True
        else:
            return False
        