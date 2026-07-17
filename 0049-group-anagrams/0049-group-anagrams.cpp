class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>>res;
        unordered_map<string,vector<string>>m;
        for(auto k:strs){
            string l=k;
            sort(k.begin(),k.end());
            m[k].push_back(l);
        }
        for(auto p:m){
            vector<string>r;
            res.push_back(p.second);

        }
return res;
    }
};