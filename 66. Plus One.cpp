class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
         //iterate from end of vector to beginning, since least significant value is stored at end of vector
         for (int i = digits.size() - 1; i >= 0; i--){ 
           
            if (digits[i] + 1 != 10){ //if adding 1 to vector won't create carry, then add 1
                digits[i] += 1;
                return digits;
            }

            digits[i] = 0; //set value to 0 for first part of number 10

            if (i == 0){
                digits.insert(digits.begin(), 1); //insert 1 at very beginning of vector
                return digits;
            }
            
         }

        return digits;
    }
};
