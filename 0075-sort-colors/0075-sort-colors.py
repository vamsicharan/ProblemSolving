class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i],nums[min] = nums[min],nums[i]
        return nums  

        # for i in range(len(nums)):
        #     var = False
        #     for j in range(0,len(nums)-1-i):
        #         if  nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        #             var = True
        #     if not var:
        #         return nums


        