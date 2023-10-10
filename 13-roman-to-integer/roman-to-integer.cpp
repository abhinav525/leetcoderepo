class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int>mapp;
        mapp['I'] = 1;
        mapp['V'] = 5;
        mapp['X'] = 10;
        mapp['L'] = 50;
        mapp['C'] = 100;
        mapp['D'] = 500;
        mapp['M'] = 1000;
        int  n=s.length();
        int ans=0;


        for(int i=0;i<n;i++){
            if(mapp[s[i]]<mapp[s[i+1]]){
                ans-=mapp[s[i]];

            }
            else{
                ans+=mapp[s[i]];
            }

        }
        return ans;

        
    }
};