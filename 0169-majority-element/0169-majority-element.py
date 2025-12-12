class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        variable = {}
        length = len(nums)/2
        for i in range(len(nums)):
            if nums[i] not in variable:
                variable[nums[i]] =1
            else:
                variable[nums[i]] +=1
        for key,val in variable.items():
            if val > length:
                return key        
        