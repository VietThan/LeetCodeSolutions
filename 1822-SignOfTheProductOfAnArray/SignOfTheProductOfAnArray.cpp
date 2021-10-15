class Solution {
public:
    int arraySign(vector<int>& nums) {
        std::vector<int>::iterator it = nums.begin();
        int sign = 1;
            
        while (it != nums.end()){
            if (*it == 0){
                return 0;
            }
            
            if (*it < 0){
                if (sign < 0){sign = 1;}
                else{sign = -1;}
            }
            
            ++it;
        }
        
        return sign;
        
    }
};
