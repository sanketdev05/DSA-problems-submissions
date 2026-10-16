class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in twosum:
                return [twosum[needed], index]
            else:
                twosum[num] = index
        