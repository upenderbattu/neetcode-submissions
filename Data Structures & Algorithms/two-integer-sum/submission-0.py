class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_list = len(nums)
        for i in range(length_list):
            for j in range(i + 1, length_list):
                add_va = nums[i] + nums[j]
                if add_va == target:
                    return [i, j]
