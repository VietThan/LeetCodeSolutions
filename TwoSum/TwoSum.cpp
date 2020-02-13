class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // unordered_map (hashmap)
        // key = number
        // value = index
        unordered_map<int, int> differences;
        
        // vector to store result
        vector<int> result;

        // iterate over nums
        for(int i = 0; i < nums.size(); ++i){
            // find the difference
            int diff = target - nums[i];
            
            // find if difference exists in hashmap
            if(differences.find(diff) != differences.end()){
                // if it does, push the index of diff/value
                // this is index of corresponding difference
                // to value of current index
                result.push_back(differences[diff]);
                // push back the value of current index
                result.push_back(i);
		return result;
            }
            
            // put the value index corresponding to key nums[i]
            differences[nums[i]] = i;
        }
        
        return result;
    
    }
    
};
