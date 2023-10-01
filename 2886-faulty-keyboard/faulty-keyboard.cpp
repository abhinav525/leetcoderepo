class Solution {
public:
    string finalString(string s) {
        int n=s.size();
        int i=0;
        while(i<n){
            if(s[i]=='i'){

                s.erase(i,1);
                
                reverse(s.begin(),s.begin()+i);
                
            }
            else{
                i++;
            }
        }
        return s;
        
    }
};