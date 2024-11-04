class Solution(object):
    def intersection(self, nums1, nums2):
        # creating sets to save only unique values in an array
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
