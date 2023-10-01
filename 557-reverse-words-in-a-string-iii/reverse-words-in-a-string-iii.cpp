class Solution {
public:
    string reverseWords(string s) {
        int left=0;
        int right=0;
        int  n=s.size();
        while(left<n){
            while(right<n && s[right]!=' '){
                right++;
               
            }
            reverse(s.begin() + left , s.begin() +  right);
            left=right+1;
            right=left;
        }
        return s;
        
    }
};