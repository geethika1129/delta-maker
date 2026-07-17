class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for (int num : nums) {
            m[num]++;
        }

        // bucket: index = frequency, value = list of numbers
        vector<vector<int>> bucket(nums.size() + 1);
        for (auto& p : m) {
            bucket[p.second].push_back(p.first);
        }

        vector<int> res;
        for (int i = bucket.size() - 1; i >= 0 && res.size() < k; i--) {
            for (int num : bucket[i]) {
                res.push_back(num);
                if (res.size() == k) break;
            }
        }
        return res;
    }
};
