//Same approach as my python submission, I used a unordered map to assign the values then check if the numeral is being used to reduce the value of the next numeral

//Worth noting that despite being an "average" solution in terms of speed and RAM usage, it's still only uses 1/3rd of the runtime and half the RAM of my python 
//solution which was allegedly faster than 98% of other python submissions

//https://leetcode.com/problems/roman-to-integer
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int>m {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}}; //define map and assign values to numerals
        int ans = 0; 

        for (int i =0; i<s.length();i++){
            cout<<m[s[i]]<<endl;
            if(i<s.length()-1 && m[s[i]]<m[s[i+1]]) //check length first to ensure there's no overflow error, then check if next value is larger
                ans-= m[s[i]]; //if next value is larger, we subtract
            else
                ans+= m[s[i]]; //if not, then we simply add
        }
        return ans;
    }
};
