class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = prices[0];
        int diff = 0;
        
        for (int i = 0; i < prices.size(); i++){
            int temp = prices[i] - min;
            if (temp > diff){
                diff = temp;
            }
            
            if (prices[i] < min){
                min = prices[i];
            }
        }
        
        return diff;
    }
};
