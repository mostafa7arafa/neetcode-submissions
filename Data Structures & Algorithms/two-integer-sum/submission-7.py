class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i+1,len(nums)):
        #         s = nums[i] + nums[j]
        #         if s == target:
        #             return [i,j]
        prevNum = {} # Value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevNum:
                return [prevNum[diff], i]
            prevNum[n] = i