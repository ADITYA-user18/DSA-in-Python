class Solution(object):
    def intersection(self, nums1, nums2):

        new = set()

        for num in nums1 and nums2:
            if num in nums1 and nums2:
                new.add(num)

        return list(new)

    