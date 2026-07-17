class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>m;
        vector<int>res;
        for(int i=0;i<nums.size();i++){
            int a = nums[i];
            int k=target-a;
            if(m.find(k)!= m.end()){
                res.push_back(m[k]);
                res.push_back(i);
            }          
            m[a]=i;

        }return res;
    }
};