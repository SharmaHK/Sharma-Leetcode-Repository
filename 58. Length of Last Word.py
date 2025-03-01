class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ending = len(s)-1

        while ending >= 0 and s[ending] == ' ':
            ending = ending - 1
        
        start = ending

        while start >= 0 and s[start] != ' ':
            start = start - 1

        return (ending - start)
