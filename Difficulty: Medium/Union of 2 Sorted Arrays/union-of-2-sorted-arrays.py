class Solution:
    def findUnion(self, a, b):
        # code here 
       new_list=list(set(a+b))
       new_list.sort()
       return new_list
       