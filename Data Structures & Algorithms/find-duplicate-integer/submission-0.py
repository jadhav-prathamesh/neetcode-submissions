class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        saw = set()
        for i in nums:
            if i in saw:
                return i
            saw.add(i)
        return -1        