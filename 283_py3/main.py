class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for index, item in enumerate(nums):
            if item == 0:
                for i in range(index + 1, len(nums)):
                    if nums[i] != 0:
                        nums[i], nums[index] = nums[index], nums[i]
                        break

"""
java

public class Solution {
    public void moveZeroes(int[] nums) {
        for(int i = 0; i < nums.length ; i++){
            if(nums[i] == 0){
                for(int j = i + 1; j < nums.length; j++){
                    if(nums[j] != 0){
                        int temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        break;
                    }
                }
                
            }
        }
        
    }
}



"""