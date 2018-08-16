"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
		
        m = len(nums1) 
        n = len(nums2) 
        i=j=0
		
        while True :
            if  i == m:
                break
            if  j == n:
                break
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            else:
                nums3.append(nums2[j])
                j = j + 1
		
        if i < m :
            for t in range(i, m):
                nums3.append(nums1[t])
		
        if j < n:
            for t in range(j, n):
                nums3.append(nums2[t])
		
        if (len(nums3)%2) == 0:
            x = int(len(nums3)/2)
            median = (nums3[x-1]+nums3[x])/2
        else:
            x = int(len(nums3)/2)
            median = (nums3[x])
        return median

def main():
	nums1 = [1, 3]
	nums2 = [2]
	obj = Solution()
	print(obj.findMedianSortedArrays(nums1, nums2))

main()