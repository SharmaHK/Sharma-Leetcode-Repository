/*
This is my c++ version of hgrsd's idea. His idea is to simply convert the instances where a numeral would subtract from a larger value (ie. IX, IV). 
Uses only a quarter of the runtime as my original C++ map solution and about 0.10MB less.
https://leetcode.com/problems/roman-to-integer/
https://stackoverflow.com/questions/4643512/replace-substring-with-another-substring-c
*/
class Solution {
public:
void replaceAll( string &s, const string &search, const string &replace ) {
    for( size_t pos = 0; ; pos += replace.length() ) {
        // Locate substring
        pos = s.find( search, pos );
        if( pos == string::npos ) break;
        // Replace by using erasing and inserting
        s.erase( pos, search.length() );
        s.insert( pos, replace );
    }
}
    int romanToInt(string s) {
        //define values
        unordered_map<char,int>m {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int ans = 0;
        replaceAll(s, "IV", "IIII");
        replaceAll(s, "IX", "VIIII");
        replaceAll(s, "XL", "XXXX");
        replaceAll(s, "XC", "LXXXX");
        replaceAll(s, "CD", "CCCC");
        replaceAll(s, "CM", "DCCCC");
        //iterate through simplified string
        for (int i =0; i<s.length(); i++)
            ans += m[s[i]];
        return ans;
    }
};
