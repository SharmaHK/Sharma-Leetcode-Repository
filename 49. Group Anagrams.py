class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}
        srt = []
        
        for i in strs:
            
            srt = str(sorted(i))
            #print(srt)
            
            if srt in ans: #if match, then pair with buddy
                ans[srt].append(i)
                #print("if:", ans[srt])
                
            else:
                ans[srt] = [i] #send to seperate group
                #print("else:",ans[srt])
                
        #print (ans.values())
                
        return list(ans.values())