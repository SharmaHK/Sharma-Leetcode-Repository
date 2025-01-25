class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      #couldn't get for i in reverse(digits) to work properly
      #translated cpp solution over to python3
        for i in range(len(digits)-1,-1,-1):
            if (digits[i]) + 1 != 10: #if value is less than 9, then add one to it and return
                digits[i] += 1
                return digits
            digits[i] = 0 #otherwise, set value to 0
            if (i == 0): #if at very beginning of value, insert 1 in front of list
                digits.insert(0,1)
                return digits
        return digits      
