class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_multi = 1
        r_multi = 1
        n = len(nums)
        l_list = [0] * n
        r_list = [0] * n

        for i in range(n):
            j = -i-1
            l_list[i] = l_multi
            r_list[j] = r_multi
            l_multi *= nums[i]
            r_multi *= nums[j]
        return [ r*l for r,l in zip(r_list,l_list)]
        