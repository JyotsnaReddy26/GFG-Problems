class Solution:
    def rangeSumQueries(self, arr, queries):
        # code here
        new_arr=[0]*len(arr)
        wanted=[]
        sumi=0
        for i in range(len(arr)):
            sumi+=arr[i]
            new_arr[i]=sumi
        for i in range(len(queries)):
            l=queries[i][0]
            r=queries[i][1]
            if l==0:
                diff=new_arr[r]
            else:
                diff=new_arr[r]-new_arr[l-1]
            wanted.append(diff)
        return wanted
        
            