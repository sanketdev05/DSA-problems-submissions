class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        same = []
        # n = len(nums)
        for i in freq1:
            if i in freq2:
                same.append(i)
        return same
        