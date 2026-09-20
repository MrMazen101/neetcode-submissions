class Solution(object):
    def twoSum(self, nums, target):
        
        # 'i' is the first pointer. It steps through the list slowly.
        for i in range(len(nums)):
            
            # 'j' is the second pointer. 
            # We tell it to always start exactly one step ahead of 'i' (i + 1)
            for j in range(i + 1, len(nums)):
                
                # Try the sum!
                if nums[i] + nums[j] == target:
                    
                    # If we find the target, return their indexes as a list
                    return [i, j] 