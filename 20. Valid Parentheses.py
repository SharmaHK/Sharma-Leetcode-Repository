#https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s):
        stack = [] 
        for i in s: 
            if i in '([{': #look for beginning characters
                stack.append(i) 
            else: #if a closing character is next and the corresponding opening character isn't on top of the stack, then we return false
                if not stack or (i == ')' and stack[-1] != '(') or (i == '}' and stack[-1] != '{') or (i == ']' and stack[-1] != '['):
                    return False 
                stack.pop() #if current character pairs with character on stack then remove character from stack 
        return not stack
#####################################################################
#First attempt
class Solution:
    def isValid(self, s: str) -> bool:

        #count number of ending and beginning characters 
        para_start = s.count('(')
        para_end = s.count(')')
        brace_start = s.count('{')
        brace_end = s.count('}')
        brack_start = s.count('[')
        brack_end = s.count(']')
        #Compare their values
        if(para_start != para_end):
            return False
        elif(brace_start != brace_end):
            return False
        elif(brack_start != brack_end):
            return False
        else:
            return True
