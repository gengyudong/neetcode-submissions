class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        difference = 0

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in storage:
                return [storage[difference], i]
            else:
                storage[nums[i]] = i
        