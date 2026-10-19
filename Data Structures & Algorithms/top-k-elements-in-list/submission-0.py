class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequncy = Counter(nums)
        k_elements = [0] * (n+1)

        for key, value in frequncy.items():

            if k_elements[value] == 0:
                k_elements[value] = [key]
            else:
                k_elements[value].append(key)

        ret = []
        for i in range(n, -1, -1):
            if k_elements[i] != 0:
                ret.extend(k_elements[i])
            if len(ret) == k:
                break
        return ret
        