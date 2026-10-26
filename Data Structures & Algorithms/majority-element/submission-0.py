class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        feq = Counter(nums)
        n = len(nums)
    
        for i in feq:
            if feq[i] > n/2:
                return i
        