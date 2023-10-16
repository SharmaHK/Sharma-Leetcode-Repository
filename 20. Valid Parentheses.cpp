//https://leetcode.com/problems/valid-parentheses
//This is a one-to-one conversion of my python solution into c++
//It ran surprisingly fast for such a simple solution. 

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for (char i : s) {
            if (i == '(' || i == '{' || i == '[') {
                stack.push(i);
            } 
            else {
                if (stack.empty() || (i == ')' && stack.top() != '(') || (i == '}' && stack.top() != '{') || (i == ']' && stack.top() != '[')) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.empty();
    }
};
