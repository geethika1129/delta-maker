class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int p=1;
        int pq=1;
        int c=0;
        vector<int>res;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0) 
            p*=nums[i]; 
            else {pq*=nums[i]; c+=1;}
        }
        for(int i=0;i<nums.size();i++){
            if(c==0) res.push_back(p/nums[i]);
            if(c==1) 
            {
                if(nums[i]!=0) res.push_back(pq/nums[i]);
                else res.push_back(p);
            }
            if(c>1){
                res.push_back(0);
            }

        }
        return res;
    }
};