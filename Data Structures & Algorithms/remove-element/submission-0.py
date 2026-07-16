class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i, j = 0, 0
        while i < k:
            if nums[i] == val:
                for j in range(i, k-1):
                    nums[j] = nums[j+1]
                k -= 1
            else:
                i += 1
        return k