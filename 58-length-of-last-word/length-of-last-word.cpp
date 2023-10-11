class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int count=0;
        int fl=0;
        int n=s.length();
        for(int i=n-1;i>=0;i--){
            if(s[i]==' ' && fl){
                break;
            }
            if(s[i]!=' '){
                count++;
                fl=count;
            }
            

        }
        return count;
    }
};