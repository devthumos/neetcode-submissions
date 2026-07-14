class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n_count = 0
        is_one = False
        max_1s = 0
        n = len(nums)
        i = 0

        while i < n:
            is_one = nums[i] == 1

            if is_one:
                n_count += is_one
            else:
                max_1s = max(n_count, max_1s)
                n_count = 0
            i += 1

        max_1s = max(n_count, max_1s)

        return max_1s