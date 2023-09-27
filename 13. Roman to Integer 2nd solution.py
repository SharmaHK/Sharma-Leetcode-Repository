#This unconventional but brilliant way to approach this problem comes from wingskh on leetcode. His idea is to simply convert the instances where a numeral would subtract from a larger value (ie. IX, IV). 
#It beat out my map solution by 10ms in some instances while only using .10 MB more RAM.
#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
      #define numerals
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
      #pure genius
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            ans += m[char]
        return ans
