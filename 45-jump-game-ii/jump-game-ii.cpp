class Solution {
public:
    int jump(vector<int>& nums) {
        int curr=0;
        int far=0;
        int n=nums.size();
        int jumps=0;
        for(int i=0;i<n-1;i++){
            far=max(far,nums[i]+i);
            if(curr==i){
                curr=far;
                jumps++;
            }
            
        }
        return jumps;
        
    }
};