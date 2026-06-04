class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in hm:
                return (hm[res],i)
            hm[n] = i
        return None        