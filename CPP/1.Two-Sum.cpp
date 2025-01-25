//solution for https://leetcode.com/problems/two-sum/
//brute force
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int vlen = nums.size(); //assigned size of nums to variable to save precious time
        for (int i = 0; i < vlen; i++){ //iterate nums[0] to nums[vlen]
            for (int j = i + 1; j < vlen; j++){ //iterate nums[i+1] to nums[vlen]
                if(nums[i]+nums[j]==target){
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
        return ans;
    }
};
