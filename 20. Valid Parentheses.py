class Solution:
    def isValid(self, s: str) -> bool:
        
        para_start = s.count('(')
        para_end = s.count(')')
        brace_start = s.count('{')
        brace_end = s.count('}')
        brack_start = s.count('[')
        brack_end = s.count(']')

        if(para_start != para_end):
            return False
        elif(brace_start != brace_end):
            return False
        elif(brack_start != brack_end):
            return False
        else:
            return True
