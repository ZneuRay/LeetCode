from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if m == 0:
            return self.getMedian(nums2)
        if n == 0:
            return self.getMedian(nums1)
        # if n == 1 and m == 1:
        #     return (nums1[0] + nums2[0]) / 2
        
        cen = (m + n) / 2
        i = 0
        j = 0
        last = 0
        cur = 0
        while 1:
            if i >= m:
                cur = nums2[j]
                j = j + 1
            elif j >= n:
                cur = nums1[i]
                i = i + 1
            elif nums1[i] > nums2[j]:
                cur = nums2[j]
                j = j + 1
            else:
                cur = nums1[i]
                i = i + 1
            if (i + j) > cen:
                break
            last = cur
        if (m + n) % 2 == 0:
            return (last + cur) / 2
        else:
            return cur
            
    def getMedian(self, nums: List[int]) -> float:
        l = len(nums)
        c = int(l / 2)
        if l % 2 == 0:
            return (nums[c - 1] + nums[c]) / 2
        else:
            return nums[c]
        
            
            
s = Solution()
print(s.findMedianSortedArrays([2], [1]))