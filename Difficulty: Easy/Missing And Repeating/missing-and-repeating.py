class Solution:
    def findTwoElement(self, arr):

        n = len(arr)
        s = sum(arr)
        sn = n * (n + 1) // 2

        s2 = sum(x * x for x in arr)
        square_sum = n * (n + 1) * (2 * n + 1) // 6

        diff = s - sn               

        square_diff = s2 - square_sum     

        sum_xy = square_diff // diff  

        repeated = (diff + sum_xy) // 2

        missing = repeated - diff

        return [repeated, missing]