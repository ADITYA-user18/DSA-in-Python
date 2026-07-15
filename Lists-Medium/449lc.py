class Solution(object):
    def intersection(self, nums1, nums2):

        d = set()

        for i in range(len(nums1)):
            if nums1[i] in nums2:

                d.add(nums1[i])

        return list(d)




    

