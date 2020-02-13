class Solution {
    public int[] twoSum(int[] nums, int target) {
        // key-value hashmap
        // key = number/differences
        // value = index
        Map<Integer, Integer> differences = new HashMap<Integer, Integer>();
        
        // int array to store results
        int[] result = new int[2];
        
        for (int i = 0; i < nums.length; ++i){
            int diff = target - nums[i];
            if (differences.containsKey(diff)){
                result[0] = differences.get(diff);
                result[1] = i;
                return result;
            }
            
            differences.put(nums[i], i);
        }
        
        return result;
        
    }
}
