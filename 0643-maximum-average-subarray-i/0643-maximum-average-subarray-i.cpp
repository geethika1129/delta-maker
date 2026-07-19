class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum=0;
        double maxi=INT_MIN;
        double avg;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        maxi=sum;
            for(int i=k;i<nums.size();i++){
                sum-=nums[i-k];
                sum+=nums[i];
            maxi = max(maxi, sum);     


        }
        return maxi/k;
    }
};