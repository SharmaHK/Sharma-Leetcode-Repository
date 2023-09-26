class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        #variable declaration
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        cleaned_key = []
        dict = {}
        result  = []
        
        #cleanse key of nonalphabetic characters
        #counter1 = 0
        for counter1 in key:
            if counter1.isalpha() and counter1 not in cleaned_key:
                cleaned_key.append(counter1)
        
        #populate dictionary with code key
        for c1, c2 in zip(cleaned_key, alphabet):
            dict[c1] = c2
        
        #translate message and add into result string
        #counter2 = 0
        for counter2 in message:
            if counter2.isalpha():
                result.append(dict[counter2]) #append translated char to string
            else:
                result.append(counter2) #append non char w/o translation

        #create translated string     
        result = "".join(result)

        return result
