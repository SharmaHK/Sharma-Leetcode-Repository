class Solution {
public:
    int lengthOfLastWord(string s) {
        using namespace std;
      //find end of string
        int ending = s.length() - 1;
      //find where last word ends, skip over spaces at end
        while (ending >= 0 && s[ending] == ' ')
            ending--;
        
        int start = ending;
      //find beginning of last word
        while (start >= 0 && s[start] != ' ')
            start--;
      
        return ending - start;
    }
};
