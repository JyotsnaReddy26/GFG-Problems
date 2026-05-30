class Solution:
    def leaders(self, arr):
        # code here
        res=[]
        max_element=0
        n=len(arr)
        for i in range(n-1,-1,-1):
            if arr[i]>=max_element:
                res.append(arr[i])
            max_element=max(max_element,arr[i])
        return res[::-1]