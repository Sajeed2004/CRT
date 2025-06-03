class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        start,end = 0,len(arr)-1
        result = -1
        while start<=end:
            mid= end-start//2
            if(arr[mid]==k):
                result= mid
                end=mid-1
            elif(k>arr[mid]):
                start = mid + 1
            else:
                end = mid - 1
        return result