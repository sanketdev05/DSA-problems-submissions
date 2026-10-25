class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        n = len(nums)

        for i in range(n):

            ans.append(nums[i])
        ans.extend(nums)

        return ans

        