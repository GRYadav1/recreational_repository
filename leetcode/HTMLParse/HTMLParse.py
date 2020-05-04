'''
Created on 22-Apr-2020

@author: gaurav
'''
import re
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
#         dict ={'&quot;':r"\\", '&apos;':'\'','&amp;':'&','&gt;':'>','&lt;':'<','&frasl;':'/'}
#         
#         pneumaText = text.split(' ')
#         
#         print(pneumaText);
#         
#         for i in range(len(pneumaText)):
#             if pneumaText[i] in dict:
#                 pneumaText[i] = dict[pneumaText[i]]
#             
#         retStr =""
#         for i in pneumaText:
#             retStr+=i
#             retStr+=' '
#             
#         retStr.rstrip()
#         
#         record = ""
#         startRecord = 0
#         endRecord = 0
#         flag = False
#         for i in range(len(retStr)):
#             
#             if(retStr[i]=='&' or flag):
#                 if(not flag):
#                     startRecord = i
#                 flag= True
#                 record+=retStr[i]
#             
#             if(flag and retStr[i]==";" and record!=""):
#                 flag = False
# #                 record+=retStr[i]
#                 endRecord=i-1
#         
#             if(record!="" and not flag and record in dict):
#                 retStr=retStr[:startRecord] + dict[record] + retStr[endRecord+1:]
#                 print(retStr)
#                 record=""
#         
#         return retStr
#         
#                 
#             
#             
#             
#         return retStr.rstrip()
        
                
        text = text.replace("&quot;",'"')
        text = text.replace("&apos;",'\'')
        
        text = text.replace("&gt;",'>')
        text = text.replace("&lt;",'<')
        text = text.replace("&frasl;",'/')
        text = text.replace("&amp;",'&')
        
        return text
        
        
        
def main():
    
    print(Solution().entityParser("&amp;gt;"))
    
main()
