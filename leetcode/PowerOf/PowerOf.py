
def checkPangram(s): 
    List = [] 
    # create list of 26 charecters and set false each entry 
    for i in range(26): 
        List.append(False) 
          
    #converting the sentence to lowercase and iterating 
    # over the sentence  
    for c in s.lower():  
        if not c == " ": 
            # make the corresponding entry True 
            List[ord(c) -ord('a')]=True 
    print(List)
    #check if any charecter is missing then return False 
    for ch in List: 
        if ch == False: 
            return False
    return True
  
# Driver Program to test above functions 
sentence = "The quick brown fox jumps very the little lazy dog"
  
if (checkPangram(sentence)): 
    print (sentence)
    print ("is a pangram") 
else: 
    print (sentence)
    print ("is not a pangram")
  