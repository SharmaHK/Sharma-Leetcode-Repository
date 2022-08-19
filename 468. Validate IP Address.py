class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        ipv6_char_list="0123456789abcdefABCDEF"
    
        sep_ip=queryIP.split('.') #ipv4
        sep_ip_2=queryIP.split(':') #ipv6
        
        #print(sep_ip)
        
        if ':' in queryIP and '.' in queryIP: #check for both decimal and colon
            return "Neither"
        
        elif len(sep_ip)==4: #check if queryIP is 4 parts after split
            
            for ctr in sep_ip:

                if len(ctr)==0:
                    return 'Neither'
                
                if len(ctr)>1 and ctr[0]=='0':
                    return 'Neither'
                
                for ctr_2 in ctr: #check if there's any non numeric characters
                    if ctr_2.isdigit() == False:
                        return 'Neither'
                
                if int(ctr) >= 256: #check if value is higher than 255
                    #print(ctr)
                    return 'Neither'
            
            return 'IPv4'
        
        elif len(sep_ip_2)==8: #check if queryIP is 8 parts after split
            
            for ctr in sep_ip_2:
                
                if len(ctr)==0: 
                    return 'Neither'
                
                elif len(ctr)>4:
                    return 'Neither'
                
                else:
                    
                    for ctr_2 in ctr: 
                        print(ctr)
                        
                        if ctr_2.isalnum(): #check if alphanumeric
                            
                            if  ctr_2 not in ipv6_char_list: #check if chars in ipv6 list
                                return 'Neither'
                        
                        else:
                            return 'Neither'
                                            
            return 'IPv6'
                        
        else:
            return 'Neither'