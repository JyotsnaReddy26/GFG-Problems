class Solution:
    def prefSum(self, arr):
        # code here
        new_arr=[0]*len(arr)
        sumi=0
        for i in range(len(arr)):
            sumi+=arr[i]
            new_arr[i]=sumi
        return new_arr
       