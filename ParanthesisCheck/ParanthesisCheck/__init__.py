from _ctypes import sizeof

def isValid(s):
    dict = { '(':1,')':1, '[':2, ']':2, '{':3, '}':3}
    stack = []
    sum = 0
    for k in range(0,len(s)):
        i = s[k]
        if (i == '(' or i== '[' or i=='{'):
            stack.append(i)
        
        else:
            if (i ==')' or i==']' or i=='}'):
                if(stack):
                    j=stack[-1]
                else: return False    
                if (dict[j]== dict[i]):
                    stack.pop()
                else: return False    
                    
    if(stack.__len__()!=0):
        return False;
    return True        
        
def main():
    
    s = '(])'
    print(isValid(s));

main()        