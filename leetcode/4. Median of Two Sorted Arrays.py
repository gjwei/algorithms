# coding: utf-8
# Author: gjwei

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, m, nums2, n = nums2, n, nums1, m

        half_length = (m + n + 1) >> 1
        imin, imax = 0, m

        while imin <= imax:
            i = (imin + imax) >> 1
            j = half_length - i
            if i < m and nums2[j - 1] > nums1[i]:  # i to small
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:  # i too bigger
                imin = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) & 1 == 1:
                    return max_of_left
                if i == m:
                    min_of_left = nums2[j]
                elif j == n:
                    min_of_left = nums1[i]
                else:
                    min_of_left = min(nums1[i], nums2[j])
                return (max_of_left + min_of_left) / 2.0
