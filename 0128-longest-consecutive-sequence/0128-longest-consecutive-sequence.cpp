class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int cnt=1;
        int max=1;
        set<int>s;
        for(int i=0;i<nums.size();i++){
            s.insert(nums[i]);
        }
        for(auto k:s){
            if(s.find(k+1)!=s.end()){
                cnt+=1;
            }
            else{
                max = std::max(max, cnt);
                 cnt=1;
            }
            
            }if(nums.size()==0) return 0;
            else return max;
        
        
    }
};