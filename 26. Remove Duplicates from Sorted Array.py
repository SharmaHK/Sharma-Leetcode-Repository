class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1

        for j in range(len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i +=1
        
        print (i)
        return i 
