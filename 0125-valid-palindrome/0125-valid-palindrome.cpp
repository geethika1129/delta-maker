class Solution {
public:
    bool ispa(string s){
        int l=0; int h=s.size()-1;
        while(l<=h){
            if(s[l]!=s[h]) return false;
            l++;
            h--;
        }
        return true;
    }
    bool isPalindrome(string s) {
        for (auto& x : s) {
        x = tolower(x);
    }
        string temp;
        for(int i=0;i<s.size();i++){
            if(s[i]>='a' && s[i]<='z'|| (s[i] >= '0' && s[i] <= '9')){
                temp+=s[i];

            }
        }
        return ispa(temp);
    }
};