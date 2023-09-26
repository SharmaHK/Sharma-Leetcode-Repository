#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        #list for numeral values
        m = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0

        for i in range(len(s)):
          #it's important that you check the length of s first in order to avoid overflow errors
          #checks if the next numeral is larger than the current numeral to determine if it "taking away" from the next numeral
            if i < len(s) - 1 and m[s[i]]<m[s[i+1]]:
                ans-=m[s[i]]
            else: #otherwise just add numeral value to ans
                ans+=m[s[i]]

        return ans
